/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        shield: {
          900: '#0b1020',
          800: '#111827',
          700: '#172033',
          500: '#36d399',
          400: '#60a5fa',
          300: '#f59e0b',
          200: '#ef4444',
        },
      },
    },
  },
  plugins: [],
}
