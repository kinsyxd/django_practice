import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
    root: './frontend',
    base: '/static/',
    build: {
        manifest: true,
        outDir: resolve(__dirname, 'static'),
        emptyOutDir: true,
        rollupOptions: {
            input: resolve(__dirname, 'frontend/main.js'),
        },
    },
    server: {
        origin: 'http://localhost:5173',
    },
});

