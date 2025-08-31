AI Microservices with LangChain

This project provides modular AI-powered microservices built using FastAPI, LangChain pipelines.
It exposes REST APIs for:

📄 Text Summarization

❓ Q&A over Documents (PDF / text)

🧭 Dynamic Learning Path Suggestion

Features

It uses open-source LLMs (OpenRouter for DeepSeek R1 chat model and models from huggingspace i.e the embedding model).

Modular microservices (services/ & utils/).

REST API endpoints (tested via Postman & curl).

Ready for deployment on Render (or any cloud).

Project Structure

.
├── Assignment-1/
   ├── main.py                # FastAPI entry point
   ├── services/
   │   ├── summarizer.py
   │   ├── qa_service.py
   │   ├── learning_path.py
   │   └── llm_client.py
   └── utils/
   |   └── document_store.py
   ├── requirements.txt
   └── README.md

⚙️ Environment Setup

1️⃣ Clone the repository

git clone https://github.com/subhajit11010/SUBHAJIT_CHAKRABORTY_INTERNSHIP_ASSIGNMENTS.git
cd SUBHAJIT_CHAKRABORTY_INTERNSHIP_ASSIGNMENTS

2️⃣ Create a virtual environment

python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows

3️⃣ Install dependencies

cd Assignment-1
pip install -r requirements.txt

4️⃣ Set up environment variables

Create a .env file in the root folder with your keys:

OPENROUTER_API_KEY=Your openrouter api key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

5️⃣ Run the server

uvicorn main:app --host 0.0.0.0 --port 8000

🔗 API Endpoints
1. 📄 Text Summarization

POST /summarize

Request:

{
  "text": "Artificial Intelligence is a rapidly growing field that combines computer science, mathematics, and domain knowledge to create systems capable of learning and decision-making. It has applications in healthcare, finance, robotics, and more.",
  "max_length": 50
}


Response:

{
    "summary": "AI combines computer science, math, and domain expertise to build systems that learn and make decisions. It's rapidly growing and applied in fields like healthcare, finance, and robotics. (24 words)"
}

2. ❓ Q&A over Documents

POST /qa

Accepts file upload (pdf, txt, md) + question query parameter.

Example (curl) Request:
curl -X POST "http://localhost:8000/qa" -F "file=@routine.pdf" -F "question=When the OOPs lab is for CSE sec3c?"

Response:

{
    "answer": "Based on the timetable for **CSE.3C (A-313)**, the OOP Lab occurs at two different times:\n\n1.  **Wednesday, Period 5:** 13:50 - 14:40\n2.  **Thursday, Period 1:** 9:40 - 10:30\n\nBoth sessions are listed as \"OOP Lab CS_SUD / CS_SS / CS_KS\"."
}

3. 🧭 Dynamic Learning Path Suggestion

POST /get_suggestions

Example Request:

{
    "background": "Machine Learning enthusiast",
    "goal": "Mastering NodeJs",
    "months": 6
}

Response:

{
    "learning_path": "### 6-Month Node.js Mastery Plan for a Machine Learning Enthusiast  \n*Designed for foundational JavaScript knowledge. Adjust pace based on prior experience.*\n\n---\n\n#### **Phase 1: Core Node.js & Async Programming (Weeks 1-4)**  \n- **Week 1: JavaScript Refresher & Node.js Setup**  \n  - Topics: ES6+ syntax (arrow functions, promises, modules), npm basics, Node runtime.  \n  - Project: Build a CLI tool (e.g., file renamer).  \n  - Checkpoint: Push code to GitHub; handle 10+ files via CLI.  \n\n- **Week 2: Asynchronous JavaScript**  \n  - Topics: Callbacks, promises, `async/await`, event loop.  \n  - Project: Create a weather app fetching data from a public API (e.g., OpenWeatherMap).  \n  - Checkpoint: Handle API errors; display data cleanly.  \n\n- **Week 3: Core Node.js Modules**  \n  - Topics: `fs`, `path`, `http`, `events`, `streams`.  \n  - Project: Static file server serving HTML/CSS.  \n  - Checkpoint: Serve 1k+ concurrent users with streams.  \n\n- **Week 4: Debugging & Testing Basics**  \n  - Topics: Debugger, `console`, Jest fundamentals.  \n  - Project: Add tests to Week 2–3 projects.  \n  - Checkpoint: Achieve 80% test coverage.  \n\n---\n\n#### **Phase 2: Backend Development (Weeks 5-10)**  \n- **Week 5: Express.js Fundamentals**  \n  - Topics: Routing, middleware, REST principles.  \n  - Project: Bookstore API (CRUD for books).  \n  - Checkpoint: API handles POST/GET/PUT/DELETE.  \n\n- **Week 6: Databases I (SQL)**  \n  - Topics: PostgreSQL, pg library, basic queries.  \n  - Project: Integrate PostgreSQL into Bookstore API.  \n  - Checkpoint: Books persist in DB; prevent SQL injection.  \n\n- **Week 7: Databases II (NoSQL)**  \n  - Topics: MongoDB, Mongoose ODM, schema design.  \n  - Project: User management system with MongoDB.  \n  - Checkpoint: Users can register/login (no auth yet).  \n\n- **Week 8: Authentication & Security**  \n  - Topics: JWT, bcrypt, cookies, CORS, Helmet.  \n  - Project: Add auth to Week 7 project (protected routes).  \n  - Checkpoint: Block unauthenticated access to endpoints.  \n\n- **Week 9: Error Handling & Logging**  \n  - Topics: Custom error middleware, Winston/morgan.  \n  - Project: Implement centralized error handling in all APIs.  \n  - Checkpoint: Errors logged; no crashed servers.  \n\n- **Week 10: REST API Optimization**  \n  - Topics: Pagination, caching (Redis), compression.  \n  - Project: Optimize Bookstore API response times.  \n  - Checkpoint: Reduce latency by 40%+ via caching.  \n\n---\n\n#### **Phase 3: Advanced Integrations (Weeks 11-18)**  \n- **Week 11: WebSockets & Real-Time Apps**  \n  - Topics: Socket.io, event-driven architecture.  \n  - Project: Live chat app or real-time dashboard.  \n  - Checkpoint: Messages sync instantly across clients.  \n\n- **Week 12: Microservices & RabbitMQ**  \n  - Topics: AMQP, message queues, decoupled services.  \n  - Project: Split Bookstore API into auth/library services.  \n  - Checkpoint: Services communicate via RabbitMQ.  \n\n- **Week 13: Docker & Containers**  \n  - Topics: Dockerfiles, containers, Docker Compose.  \n  - Project: Containerize Week 12 microservices.  \n  - Checkpoint: Run full stack via `docker-compose up`.  \n\n- **Week 14: Testing Deep Dive**  \n  - Topics: Integration/e2e tests (Supertest), mocking.  \n  - Project: Achieve 90%+ test coverage for all services.  \n  - Checkpoint: Tests pass in CI (GitHub Actions).  \n\n- **Week 15: TypeScript in Node.js**  \n  - Topics: Basic types, interfaces, `ts-node`.  \n  - Project: Migrate Bookstore API to TypeScript.  \n  - Checkpoint: Zero `any` types; typed request/response.  \n\n- **Week 16: GraphQL**  \n  - Topics: Apollo Server, schemas, resolvers.  \n  - Project: Convert REST API to GraphQL.  \n  - Checkpoint: Client can query nested book/author data.  \n\n- **Week 17: ML Integration I**  \n  - Topics: TensorFlow.js, Python/Node bridges (child processes).  \n  - Project: API that runs a Python ML model (e.g., sentiment analysis).  \n  - Checkpoint: Node passes data to Python script; returns prediction.  \n\n- **Week 18: ML Integration II**  \n  - Topics: Pre-trained models, ONNX runtime.  \n  - Project: Deploy an image classifier via Express endpoint.  \n  - Checkpoint: User uploads image → returns predictions.  \n\n---\n\n#### **Phase 4: Deployment & Scalability (Weeks 19-26)**  \n- **Week 19: Cloud Deployment (AWS/GCP)**  \n  - Topics: EC2/Compute Engine, S3/Cloud Storage.  \n  - Project: Deploy ML-API to cloud VM.  \n  - Checkpoint: API accessible via public IP.  \n\n- **Week 20: Serverless**  \n  - Topics: AWS Lambda, serverless frameworks.  \n  - Project: Convert image classifier to serverless function.  \n  - Checkpoint: Function triggers via HTTP; scales automatically.  \n\n- **Week 21: Kubernetes**  \n  - Topics: Pods, deployments, services.  \n  - Project: Container orchestration for microservices.  \n  - Checkpoint: Services scale with load.  \n\n- **Week 22: Monitoring & DevOps**  \n  - Topics: Prometheus, Grafana, health checks.  \n  - Project: Add monitoring to Kubernetes cluster.  \n  - Checkpoint: Dashboard displays CPU/RAM/error rates.  \n\n- **Week 23: Performance Tuning**  \n  - Topics: Load testing (Artillery), profiling, clustering.  \n  - Project: Optimize ML-API for 10k RPM.  \n  - Checkpoint: Latency < 100ms at 1k RPM.  \n\n- **Week 24: Security Hardening**  \n  - Topics: OWASP Top 10, rate limiting, secrets management.  \n  - Project: Audit all projects; fix vulnerabilities.  \n  - Checkpoint: Zero critical issues (Snyk scan).  \n\n- **Week 25-26: Capstone Project**  \n  - Project: Full-stack app (e.g., real-time ML dashboard).  \n    - Frontend: React/Vue  \n    - Backend: Node + Express + GraphQL  \n    - ML: Python model inference  \n    - Infrastructure: Docker/Kubernetes on cloud  \n  - Checkpoint:  \n    - Demo day: Present project with live deployment.  \n    - Code review: 100% test coverage, monitoring, CI/CD.  \n\n---\n\n#### **Success Metrics**  \n1. **Weekly**: Complete projects + checkpoints.  \n2. **Monthly**: Portfolio review (GitHub activity, deployed projects).  \n3. **Final**:  \n   - Capstone deployed publicly.  \n   - Performance: < 200ms latency at 5k RPM.  \n   - Security: A+ on Mozilla Observatory scan.  \n\n> **Tools to Use**: VS Code, Postman, Docker, Jest, GitHub Actions, Prometheus.  \n> **Tips**:  \n> - Revisit ML concepts in Weeks 17–18 to bridge with Node.js.  \n> - Join Node.js communities (e.g., Discord, Stack Overflow).  \n> - Document learnings in a blog/portfolio."
}


🧪 Testing with Postman

Import the provided Postman Collection (postman_collection.json)

Test endpoints locally (http://localhost:8000) or via any cloud services

📜 License

MIT License. Free to use & modify.