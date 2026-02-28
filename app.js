const API_BASE = "https://otp-hub.onrender.com";
const out = document.getElementById('out');

function log(x){ out.textContent = typeof x === 'string' ? x : JSON.stringify(x,null,2); }

async function post(path, body){
  const r = await fetch(API_BASE + path, { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(body)});
  const t = await r.text();
  let data;
  try { data = JSON.parse(t); } catch { data = t; }
  return { status: r.status, data };
}

document.getElementById('sendBtn').onclick = async () => {
  const phone = document.getElementById('phone').value.trim();
  const channel = document.getElementById('channel').value;
  log('Sending...');
  log(await post('/otp/send', { phone, channel }));
};

document.getElementById('verifyBtn').onclick = async () => {
  const phone = document.getElementById('vPhone').value.trim();
  const code = document.getElementById('code').value.trim();
  log('Verifying...');
  log(await post('/otp/verify', { phone, code }));
};
