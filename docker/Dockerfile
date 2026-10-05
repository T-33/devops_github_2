# Stage 1: Build
FROM node:22-alpine AS builder

USER node
WORKDIR /home/node/app

COPY --chown=node:node package*.json ./
RUN npm ci

COPY --chown=node:node . .
RUN npm run build

# Stage 2: Production Server
FROM node:22-alpine AS runner

RUN npm install -g serve

USER node
WORKDIR /home/node/app

COPY --chown=node:node --from=builder /home/node/app/dist ./dist

EXPOSE 3000

CMD ["serve", "-s", "dist", "-l", "3000"]
