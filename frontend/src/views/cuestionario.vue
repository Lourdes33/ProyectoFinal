<template>
  <div class="questionnaire-wrapper">
    <div class="questionnaire-container">
      
      <!-- Encabezado fijo con el progreso -->
      <div class="header-sticky">
        <div class="progress-info">
          <span class="progress-text">Completado: {{ answeredCount }} de {{ preguntas.length }}</span>
          <span v-if="allAnswered" class="ready-text">¡Listo para enviar!</span>
        </div>
        <div class="progress-bar">
          <div class="progress-fill" :style="{ width: progressPercentage + '%' }"></div>
        </div>
      </div>

      <!-- Lista de todas las preguntas -->
      <div class="questions-list">
        <div 
          v-for="(pregunta, qIndex) in preguntas" 
          :key="pregunta.id" 
          class="question-card"
        >
          <h2>{{ qIndex + 1 }}. {{ pregunta.texto }}</h2>
          
          <div class="options-list">
            <label 
              v-for="(opcion, oIndex) in pregunta.opciones" 
              :key="oIndex"
              class="option-label"
              :class="{ 'selected': respuestas[pregunta.id] === opcion.valor }"
            >
              <input 
                type="radio" 
                :name="'pregunta-' + pregunta.id" 
                :value="opcion.valor" 
                v-model="respuestas[pregunta.id]"
              />
              {{ opcion.texto }}
            </label>
          </div>
        </div>
      </div>

      <!-- Botón final -->
      <div class="submit-section">
        <button 
          @click="submitTest" 
          :disabled="!allAnswered || isSubmitting"
          class="btn-success"
        >
          {{ isSubmitting ? 'Analizando respuestas...' : 'Finalizar y Ver Resultado' }}
        </button>
        <p v-if="!allAnswered" class="warning-text">
          Debes responder todas las preguntas para continuar.
        </p>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

// Preguntas simuladas
const preguntas = [
  {
    id: 1,
    texto: '¿Qué actividad disfrutas más en tu tiempo libre?',
    opciones: [
      { texto: 'Armar o desarmar equipos electrónicos', valor: 'A' },
      { texto: 'Leer sobre historia o psicología', valor: 'B' },
      { texto: 'Dibujar, pintar o crear diseños', valor: 'C' }
    ]
  },
  {
    id: 2,
    texto: 'Cuando trabajas en equipo, prefieres...',
    opciones: [
      { texto: 'Organizar los datos y la lógica del proyecto', valor: 'A' },
      { texto: 'Mediar en conflictos y escuchar a los demás', valor: 'B' },
      { texto: 'Aportar las ideas visuales o creativas', valor: 'C' }
    ]
  },
  {
    id: 3,
    texto: '¿Cómo prefieres resolver un problema complejo?',
    opciones: [
      { texto: 'Buscando patrones y usando matemáticas', valor: 'A' },
      { texto: 'Analizando el comportamiento humano involucrado', valor: 'B' },
      { texto: 'Buscando una solución innovadora y fuera de lo común', valor: 'C' }
    ]
  }
];

const respuestas = ref({});
const isSubmitting = ref(false);

// Calculamos cuántas preguntas tienen respuesta
const answeredCount = computed(() => Object.keys(respuestas.value).length);

// Verificamos si ya se respondieron todas
const allAnswered = computed(() => answeredCount.value === preguntas.length);

// Calculamos el porcentaje para la barra de progreso
const progressPercentage = computed(() => (answeredCount.value / preguntas.length) * 100);

const submitTest = async () => {
  isSubmitting.value = true;
  
  try {
    // Enviamos las respuestas a Flask
    const response = await fetch('http://127.0.0.1:5000/api/test/evaluar', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(respuestas.value)
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error('Hubo un problema al evaluar el test.');
    }

    // Guardamos el resultado en SessionStorage temporalmente
    // para que la vista de resultados (ResultView) pueda leerlo
    sessionStorage.setItem('resultadoVocacional', JSON.stringify(data.resultado));

    // Redirigimos a la pantalla de resultados
    router.push('/resultado');

  } catch (error) {
    alert("Ocurrió un error de conexión: " + error.message);
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<style scoped>
.questionnaire-wrapper {
  background-color: #f4f7f6;
  min-height: 100vh;
  padding: 40px 20px;
  font-family: Arial, sans-serif;
}

.questionnaire-container {
  max-width: 700px;
  margin: 0 auto;
}

/* Encabezado fijo en la parte superior para no perder de vista el progreso */
.header-sticky {
  position: sticky;
  top: 0;
  background-color: #f4f7f6;
  padding: 10px 0 20px 0;
  z-index: 10;
}

.progress-info {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  font-size: 0.9em;
  font-weight: bold;
}

.progress-text { color: #666; }
.ready-text { color: #28a745; }

.progress-bar {
  width: 100%;
  height: 10px;
  background-color: #e9ecef;
  border-radius: 5px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background-color: #007bff;
  transition: width 0.4s ease;
}

.questions-list {
  display: flex;
  flex-direction: column;
  gap: 30px; /* Separación entre cada pregunta */
}

.question-card {
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

h2 {
  color: #333;
  margin-top: 0;
  margin-bottom: 20px;
  font-size: 1.3em;
}

.options-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.option-label {
  padding: 15px;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
  color: #444;
}

.option-label:hover {
  border-color: #b8daff;
  background-color: #f1f7fd;
}

.option-label.selected {
  border-color: #007bff;
  background-color: #e7f1ff;
  font-weight: bold;
  color: #0056b3;
}

.option-label input[type="radio"] {
  display: none;
}

.submit-section {
  margin-top: 40px;
  text-align: center;
  padding-bottom: 40px;
}

.btn-success {
  background-color: #28a745;
  color: white;
  border: none;
  padding: 15px 40px;
  font-size: 1.2em;
  font-weight: bold;
  border-radius: 8px;
  cursor: pointer;
  width: 100%;
  max-width: 400px;
  transition: background-color 0.2s;
}

.btn-success:hover:not(:disabled) { background-color: #218838; }

.btn-success:disabled {
  background-color: #a5d8ad;
  cursor: not-allowed;
}

.warning-text {
  color: #dc3545;
  margin-top: 15px;
  font-size: 0.9em;
}
</style>