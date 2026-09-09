<template>
  <div class="tarjeta" style="max-width: 600px; margin: 40px auto;">
    <h2>Test de Orientación Vocacional</h2>
    <p>Responde las siguientes preguntas para descubrir tu perfil académico.</p>
  </div>
  <div class="questionnaire-wrapper">
    <div class="questionnaire-card">
      
      <!-- Barra de progreso y contador -->
      <div class="header">
        <span class="progress-text">Pregunta {{ currentIndex + 1 }} de {{ preguntas.length }}</span>
        <div class="progress-bar">
          <div class="progress-fill" :style="{ width: progressPercentage + '%' }"></div>
        </div>
      </div>

      <!-- Pregunta actual -->
      <div class="question-container">
        <h2>{{ currentQuestion.texto }}</h2>
        
        <div class="options-list">
          <label 
            v-for="(opcion, index) in currentQuestion.opciones" 
            :key="index"
            class="option-label"
            :class="{ 'selected': respuestas[currentQuestion.id] === opcion.valor }"
          >
            <input 
              type="radio" 
              :name="'pregunta-' + currentQuestion.id" 
              :value="opcion.valor" 
              v-model="respuestas[currentQuestion.id]"
            />
            {{ opcion.texto }}
          </label>
        </div>
      </div>

      <!-- Controles de navegación -->
      <div class="navigation-buttons">
        <button 
          @click="prevQuestion" 
          :disabled="currentIndex === 0"
          class="btn-secondary"
        >
          Anterior
        </button>
        
        <button 
          v-if="!isLastQuestion" 
          @click="nextQuestion" 
          :disabled="!respuestas[currentQuestion.id]"
          class="btn-primary"
        >
          Siguiente
        </button>

        <button 
          v-else 
          @click="submitTest" 
          :disabled="!respuestas[currentQuestion.id] || isSubmitting"
          class="btn-success"
        >
          {{ isSubmitting ? 'Analizando...' : 'Finalizar y Ver Resultado' }}
        </button>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

// 1. Preguntas simuladas (Mock)
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

// 2. Estado del componente
const currentIndex = ref(0);
const respuestas = ref({}); // Guardará { 1: 'A', 2: 'B', ... }
const isSubmitting = ref(false);

// 3. Propiedades computadas
const currentQuestion = computed(() => preguntas[currentIndex.value]);
const isLastQuestion = computed(() => currentIndex.value === preguntas.length - 1);
const progressPercentage = computed(() => ((currentIndex.value + 1) / preguntas.length) * 100);

// 4. Métodos de navegación
const nextQuestion = () => {
  if (currentIndex.value < preguntas.length - 1) currentIndex.value++;
};

const prevQuestion = () => {
  if (currentIndex.value > 0) currentIndex.value--;
};

const submitTest = () => {
  isSubmitting.value = true;
  
  // Simulamos el envío al backend (Node.js -> Python)
  setTimeout(() => {
    console.log("Respuestas enviadas al motor de inferencia:", respuestas.value);
    // Aquí luego recibiremos el UUID del resultado y redirigiremos
    alert("¡Test completado! (Aquí se mostrará el resultado en el futuro)");
    isSubmitting.value = false;
    router.push('/'); // Volvemos al inicio por ahora
  }, 1500);
};
</script>

<style scoped>
.questionnaire-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f4f7f6;
  padding: 20px;
}

.questionnaire-card {
  background: white;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.05);
  width: 100%;
  max-width: 600px;
}

.header {
  margin-bottom: 30px;
}

.progress-text {
  display: block;
  margin-bottom: 10px;
  font-size: 0.9em;
  color: #666;
  font-weight: bold;
}

.progress-bar {
  width: 100%;
  height: 8px;
  background-color: #e9ecef;
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background-color: #007bff;
  transition: width 0.3s ease;
}

h2 {
  color: #333;
  margin-bottom: 25px;
  font-size: 1.4em;
  line-height: 1.4;
}

.options-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.option-label {
  display: block;
  padding: 15px 20px;
  border: 2px solid #e9ecef;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 1.1em;
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

/* Ocultamos el radio button por defecto porque ya estilizamos el contenedor */
.option-label input[type="radio"] {
  display: none;
}

.navigation-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 40px;
  padding-top: 20px;
  border-top: 1px solid #eee;
}

button {
  padding: 12px 25px;
  border: none;
  border-radius: 6px;
  font-size: 1em;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.2s;
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn-secondary {
  background-color: #6c757d;
  color: white;
}
.btn-secondary:hover:not(:disabled) { background-color: #5a6268; }

.btn-primary {
  background-color: #007bff;
  color: white;
}
.btn-primary:hover:not(:disabled) { background-color: #0056b3; }

.btn-success {
  background-color: #28a745;
  color: white;
}
.btn-success:hover:not(:disabled) { background-color: #218838; }
</style>
