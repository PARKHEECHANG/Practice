import Router from 'koa-router';
import colors from './colors';
import auth from './auth';

const api = new Router();

api.use('/colors', colors.routes());
api.use('/auth', auth.routes());

// 라우터를 내보냅니다.
export default api;
