# Build stage
FROM node:23-alpine AS build-stage 


ARG APP_CACHEBUST=1
COPY ./app /app
WORKDIR /app
RUN npm install --legacy-peer-deps
RUN npm run build


# Production Stage
FROM nginx:alpine AS production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY ./rilyn /usr/share/nginx/rilyn
COPY setup_files/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY setup_files/certs /etc/nginx/certs
CMD ["nginx", "-g" ,"daemon off;"]

