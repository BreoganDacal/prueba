# Neon + Vercel Fullstack Example

This is an example project demonstrating a fullstack web app with:

- Backend: Node.js + Express API connected to Neon Postgres
- Frontend: React app deployed on Vercel calling the backend API

## Setup and Deployment Instructions

### 1. Setup Neon Postgres Database

- Sign up at https://neon.tech and create a new project.
- Create a new database and get the connection string (DATABASE_URL).
- Make sure to allow connections from your backend deployment.

### 2. Backend Setup

- Navigate to the `backend` directory.
- Create a `.env` file with the following content:

```
DATABASE_URL=your_neon_connection_string
PORT=3001
```

- Install dependencies:

```bash
npm install
```

- Run locally:

```bash
npm run dev
```

### 3. Frontend Setup

- Navigate to the `frontend` directory.
- Create a `.env` file with the following content:

```
REACT_APP_BACKEND_URL=http://localhost:3001
```

- Install dependencies:

```bash
npm install
```

- Run locally:

```bash
npm start
```

### 4. Deploy Backend

- You can deploy the backend on platforms like Railway, Render, or Vercel Serverless Functions.
- Make sure to set the `DATABASE_URL` environment variable in the deployment platform.
- The backend should be accessible via a public URL, e.g., `https://your-backend-url.com`.

### 5. Deploy Frontend on Vercel

- Push the frontend code to a GitHub repository.
- Import the repository in Vercel.
- Set the environment variable `REACT_APP_BACKEND_URL` to your backend public URL.
- Deploy the frontend.

### 6. Test

- Visit your frontend URL on Vercel.
- It should display the current time fetched from the backend connected to Neon.

---

This example demonstrates how to connect a Neon Postgres backend with a React frontend deployed on Vercel.
