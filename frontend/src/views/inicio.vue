<script setup>
import { ref } from 'vue'

const dni = ref('')
const password = ref('')
const showPassword = ref(false)

const iniciarSesion = async () => {
  // Aquí integrarás el fetch hacia la ruta POST de Flask
  console.log('Intentando iniciar sesión con DNI:', dni.value)
}

const alternarContrasena = () => {
  showPassword.value = !showPassword.value
}
</script>

<template>
  <div class="login-layout">
    <!-- Barra de Navegación -->
    <header class="navbar">
      <div class="nav-left"></div>
      <nav class="nav-right">
        <a href="#">Nosotros</a>
        <a href="#">Contacto</a>
        <button class="btn-cuestionario" @click="$router.push('/cuestionario')">CUESTIONARIO</button>
        <button class="btn-registrarse" disabled title="Solo asignación interna">Registrarse</button>
      </nav>
    </header>

    <!-- Contenido Principal -->
    <main class="main-container">
      <!-- Espacio superior (Placeholder para logo) -->
      <img src="../assets/FACENA.png" alt="Logo-FaCENA" class="logo-FaCENA" />

      <!-- Tarjeta de Login -->
      <div class="login-card">
        <h2>Iniciar Sesión</h2>
        
        <form @submit.prevent="iniciarSesion">
          <div class="form-group">
            <label for="dni">DNI</label>
            <input 
              type="text" 
              id="dni" 
              v-model="dni" 
              placeholder="Ingrese su DNI" 
              required 
            />
          </div>

          <div class="form-group">
            <label for="password">Contraseña</label>
            <div class="password-input-container">
              <input 
                :type="showPassword ? 'text' : 'password'" 
                id="password" 
                v-model="password" 
                placeholder="Ingrese su contraseña" 
                required 
              />
              <button 
                type="button" 
                class="btn-eye" 
                @click="alternarContrasena"
                aria-label="Mostrar contraseña"
              >
                <!-- Icono de ojo SVG -->
                <svg v-if="!showPassword" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line></svg>
              </button>
            </div>
          </div>

          <button type="submit" class="btn-ingresar">Ingresar</button>
        </form>
        
        <div class="enlace-recuperar">
          <a href="#">¿Olvidaste tu contraseña?</a>
        </div>
      </div>
    </main>
  </div>
</template>

<style scoped>
/* Reset básico para asegurar que ocupe toda la pantalla */
.login-layout {
  min-height: 100vh;
  background: linear-gradient(135deg, #e6f0fa 0%, #f4f8fc 100%);
  display: flex;
  flex-direction: column;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Barra de Navegación */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #ffffff;
  padding: 15px 40px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.nav-right {
  display: flex;
  align-items: center;
  gap: 25px;
}

.nav-right a {
  text-decoration: none;
  color: #333;
  font-weight: 500;
  font-size: 0.9rem;
}

.btn-cuestionario {
  background-color: #1062b0;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  font-weight: 600;
  font-size: 0.85rem;
  cursor: pointer;
}

.btn-registrarse {
  background-color: transparent;
  color: #333;
  border: 1px solid #ccc;
  padding: 8px 16px;
  border-radius: 4px;
  font-weight: 500;
  font-size: 0.85rem;
  cursor: not-allowed;
  opacity: 0.6;
}

/* Contenedor Principal */
.main-container {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

/* Placeholder del Logo Superior */
.logo-FaCENA {
  width: 90px; 
  height: auto; 
  margin-bottom: 30px;
  object-fit: contain;
}

/* Tarjeta del Formulario */
.login-card {
  background-color: #eeacac;
  padding: 40px;
  border-radius: 8px;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.05);
  width: 100%;
  max-width: 380px;
}

.login-card h2 {
  color: #000000;
  text-align: center;
  font-size: 1.4rem;
  margin-bottom: 25px;
  margin-top: 0;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  font-size: 0.85rem;
  font-weight: 600;
  color: #333;
  margin-bottom: 8px;
}

.form-group input {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 0.9rem;
  box-sizing: border-box;
  outline: none;
  transition: border-color 0.2s;
}

.form-group input:focus {
  border-color: #1062b0;
}

/* Contenedor del Input de Contraseña */
.password-input-container {
  position: relative;
  display: flex;
  align-items: center;
}

.password-input-container input {
  padding-right: 40px; /* Espacio para el icono */
}

.btn-eye {
  position: absolute;
  right: 10px;
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
}

/* Botón Principal */
.btn-ingresar {
  width: 100%;
  background-color: #b01010;
  color: white;
  border: none;
  padding: 12px;
  border-radius: 6px;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  margin-top: 10px;
  transition: background-color 0.2s;
}

.btn-ingresar:hover {
  background-color: #0c4d8a;
}

/* Enlace Inferior */
.enlace-recuperar {
  text-align: center;
  margin-top: 20px;
}

.enlace-recuperar a {
  color: #000000;
  font-size: 0.85rem;
  text-decoration: none;
}

.enlace-recuperar a:hover {
  color: #1062b0;
  text-decoration: underline;
}
</style>