<template>
  <div class="result-wrapper">
    <div class="result-card">
      
      <div class="icon-container">
        🎓
      </div>
      
      <h1>Tu Perfil Vocacional</h1>
      <p class="subtitle">Basado en el análisis de tus respuestas</p>

      <div class="primary-result">
        <h2>{{ mockResultado.areaPrincipal }}</h2>
        <p class="description">{{ mockResultado.descripcion }}</p>
      </div>

      <div class="secondary-results">
        <h3>Áreas afines a considerar:</h3>
        <ul>
          <li v-for="(area, index) in mockResultado.areasSecundarias" :key="index">
            {{ area }}
          </li>
        </ul>
      </div>

      <div class="action-buttons">
        <button @click="goHome" class="btn-outline">Volver al Inicio</button>
        <button @click="printResult" class="btn-primary">Guardar Resultado</button>
      </div>

    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

// Simulación del resultado que devolvería el backend (Node.js -> Python)
const mockResultado = {
  areaPrincipal: 'Ingeniería y Ciencias Exactas',
  descripcion: 'Tienes una fuerte inclinación hacia el razonamiento lógico, la resolución de problemas complejos y el análisis de datos. Disfrutas entender cómo funcionan las cosas y buscar soluciones eficientes.',
  areasSecundarias: [
    'Desarrollo de Software e Informática',
    'Arquitectura y Diseño Industrial'
  ]
};

const goHome = () => {
  router.push('/');
};

const printResult = () => {
  // En una app real, esto podría generar un PDF o copiar el link único (UUID)
  window.print();
};
</script>

<style scoped>
.result-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f4f7f6;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.result-card {
  background: white;
  padding: 50px 40px;
  border-radius: 12px;
  box-shadow: 0 8px 25px rgba(0,0,0,0.1);
  max-width: 600px;
  text-align: center;
  width: 100%;
}

.icon-container {
  font-size: 4em;
  margin-bottom: 10px;
}

h1 {
  color: #2c3e50;
  margin: 0;
  font-size: 2em;
}

.subtitle {
  color: #666;
  margin-top: 5px;
  margin-bottom: 30px;
}

.primary-result {
  background-color: #e7f1ff;
  border: 2px solid #b8daff;
  border-radius: 10px;
  padding: 30px 20px;
  margin-bottom: 30px;
}

.primary-result h2 {
  color: #0056b3;
  margin-top: 0;
  font-size: 1.6em;
}

.description {
  color: #444;
  line-height: 1.6;
  margin-bottom: 0;
  font-size: 1.1em;
}

.secondary-results {
  text-align: left;
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 30px;
}

.secondary-results h3 {
  margin-top: 0;
  color: #333;
  font-size: 1.1em;
}

.secondary-results ul {
  margin: 0;
  padding-left: 20px;
  color: #555;
}

.secondary-results li {
  margin-bottom: 8px;
}

.action-buttons {
  display: flex;
  gap: 15px;
  justify-content: center;
}

button {
  padding: 12px 25px;
  border-radius: 6px;
  font-size: 1em;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.2s;
  flex: 1;
}

.btn-outline {
  background-color: transparent;
  color: #6c757d;
  border: 2px solid #6c757d;
}
.btn-outline:hover {
  background-color: #6c757d;
  color: white;
}

.btn-primary {
  background-color: #007bff;
  color: white;
  border: 2px solid #007bff;
}
.btn-primary:hover {
  background-color: #0056b3;
  border-color: #0056b3;
}

/* Ocultar botones al imprimir */
@media print {
  .action-buttons {
    display: none;
  }
  .result-wrapper {
    background-color: white;
  }
  .result-card {
    box-shadow: none;
  }
}
</style>