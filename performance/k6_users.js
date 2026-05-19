// Phase 6 performance scenario for ReqRes user endpoints
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,
  duration: '30s',
  thresholds: {
    http_req_failed: ['rate<0.05'],
    http_req_duration: ['p(95)<800'],
  },
};

const BASE_URL = __ENV.BASE_URL || 'https://reqres.in';

export default function () {
  const listUsers = http.get(`${BASE_URL}/api/users?page=1`, {
    tags: { name: 'GET /api/users?page=1' },
  });

  check(listUsers, {
    'list users status is 200': (r) => r.status === 200,
  });

  const singleUser = http.get(`${BASE_URL}/api/users/2`, {
    tags: { name: 'GET /api/users/2' },
  });

  check(singleUser, {
    'single user status is 200': (r) => r.status === 200,
  });

  sleep(1);
}
