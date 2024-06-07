import axios from "axios";
import qs from "qs";

const ApiService = {
  init() {
    axios.defaults.timeout = 300000;
    axios.defaults.baseURL = "http://127.0.0.1:8000"; // API bağlantı adresini burada belirtiliyor bağlanabilmek için bu adresi düzenleyin...
  },

  query(resource, params) {
    return axios.get(resource, { params }).catch((error) => {
      throw new Error(`API Query Error: ${error}`);
    });
  },

  get(resource) {
    return axios.get(resource).catch((error) => {
      throw new Error(`API GET Error: ${error}`);
    });
  },

  post(resource, params) {
    return axios.post(resource, params).catch((error) => {
      throw new Error(`API POST Error: ${error}`);
    });
  },

  postFile(resource, params) {
    const headers = {
      "Content-Type": "multipart/form-data",
    };
    return axios.post(resource, params, { headers }).catch((error) => {
      throw new Error(`API POST Error: ${error}`);
    });
  },

  postBody(resource, params) {
    return axios.post(resource, qs.stringify(params)).catch((error) => {
      throw new Error(`API POST Error: ${error}`);
    });
  },

  update(resource, slug, params) {
    return axios.put(`${resource}/${slug}`, params).catch((error) => {
      throw new Error(`API Update Error: ${error}`);
    });
  },

  put(resource, params) {
    return axios.put(resource, params).catch((error) => {
      throw new Error(`API Put Error: ${error}`);
    });
  },

  patch(resource, params) {
    return axios.patch(resource, params).catch((error) => {
      throw new Error(`API Patch Error: ${error}`);
    });
  },

  delete(resource) {
    return axios.delete(resource).catch((error) => {
      throw new Error(`API Delete Error: ${error}`);
    });
  },
};

ApiService.init();

export default ApiService;
