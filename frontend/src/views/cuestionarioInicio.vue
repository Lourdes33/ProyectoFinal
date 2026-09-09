<template>
  <div class="welcome-wrapper">
    <div class="welcome-card">
      <h1>
        Sistema de Orientación Vocacional
      </h1>

      <h2>
        Facultad de Ciencias Exactas y Naturales y Agrimensura - UNNE
      </h2>

      <p class="descripcion">
        Descubrí qué carreras de la Facultad de Ciencias Exactas y Naturales y Agrimensura podrían ser compatibles
        con tus intereses, preferencias y características personales.
      </p>      

      <div class="informacion">
         <p>
           ✓ Cuestionario anónimo
         </p>

       <p>
          ✓ No necesitás registrarte
        </p>

        <p>
          ✓ Resultados orientativos
        </p>
      </div>

      <button @click="iniciarTest" class="start-button">
         Comenzar el Cuestionario
      </button>
      <p class="aviso">
        Las recomendaciones obtenidas son orientativas y no constituyen
        un diagnóstico psicológico ni determinan qué carrera debés elegir.
      </p>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const iniciarTest = () => {
  router.push('/cuestionario');
};
</script>

<style scoped>
.welcome-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f4f7f6;
  font-family: Arial, sans-serif;
  padding: 20px;
}

.welcome-card {
  background: white;
  padding: 50px 40px;
  border-radius: 12px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
  max-width: 600px;
  text-align: center;
}

h1 {
  color: #2c3e50;
  margin-top: 0;
  font-size: 2.2em;
}

.description {
  color: #555;
  font-size: 1.1em;
  line-height: 1.6;
  margin: 20px 0;
}

.info-list {
  text-align: left;
  background-color: #f8f9fa;
  padding: 20px 20px 20px 40px;
  border-radius: 8px;
  margin-bottom: 30px;
  color: #444;
}

.info-list li {
  margin-bottom: 10px;
}

.start-button {
  background-color: #28a745;
  color: white;
  border: none;
  padding: 15px 30px;
  font-size: 1.2em;
  font-weight: bold;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.1s;
  width: 100%;
}

.start-button:hover {
  background-color: #218838;
}

.start-button:active {
  transform: scale(0.98);
}
</style>