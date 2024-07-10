import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  define: {
    'process.env.BACKEND_API_URL': JSON.stringify(process.env.BACKEND_API_URL)
  },
  devServer: {
    allowedHosts: 'all',
    client: {
        webSocketURL: 'auto://0.0.0.0:0/ws'
    }
  },
})