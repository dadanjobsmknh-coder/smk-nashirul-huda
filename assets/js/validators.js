export const text=(value,fallback='[DATA BELUM TERSEDIA]')=>typeof value==='string'&&value.trim()?value.trim():fallback;
export const publicItems=items=>Array.isArray(items)?items.filter(item=>item.status==='publish'&&item.public!==false&&item.verificationStatus!=='needs-review'):[];
export const safeUrl=value=>{try{const u=new URL(value,location.origin);return ['http:','https:'].includes(u.protocol)?u.href:'#';}catch{return '#';}};
export const escapeHTML=value=>String(value??'').replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
