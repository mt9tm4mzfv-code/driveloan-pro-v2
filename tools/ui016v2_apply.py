from pathlib import Path

p = Path('index.html')
s = p.read_text()

# Protected blocks: UI changes must not alter these computation/clipboard sections.
f0 = s[s.index('Ir='):s.index(',ae=', s.index('Ir='))]
cb0 = s[s.index('Go=async'):s.index(',Zf=', s.index('Go=async'))]

def once(old, new, label):
    global s
    n = s.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected 1 match, got {n}')
    s = s.replace(old, new, 1)

once(
    '[resetWasClicked,setResetWasClicked]=V.useState(!1),We=',
    '[resetWasClicked,setResetWasClicked]=V.useState(!1),[brand,setBrand]=V.useState("Mitsubishi"),[customBrand,setCustomBrand]=V.useState(""),[customModel,setCustomModel]=V.useState(""),We=',
    'state'
)

once(
    'Gf=()=>{r("XPANDER CROSS"),u(1500000),o(38000),f(!1),m("White Pearl"),k(15000),c(5),d(57),C(20),z(17),D(150000),_e(10),$o(25000)}',
    'TM={"Vios XLE CVT":842000,"Vios XE":900000,"Innova E":1290000,"Fortuner G":1756000,"Hilux G":1350000,"Rush G":1135000},setBrandChoice=(L,U)=>{setBrand(L);if(L==="Toyota"){let G=TM[U]||TM["Vios XLE CVT"];r(U||"Vios XLE CVT"),u(G),o(0),f(!1)}else if(L==="Honda"){r(""),u(0),o(0),f(!1)}else if(L==="Custom"){r(customModel||""),u(0),o(0),f(!1)}else{r("XPANDER CROSS"),u(1500000),o(38000),f(!1),m("White Pearl"),k(15000)}},Gf=()=>{setBrand("Mitsubishi"),setCustomBrand(""),setCustomModel(""),r("XPANDER CROSS"),u(1500000),o(38000),f(!1),m("White Pearl"),k(15000),c(5),d(57),C(20),z(17),D(150000),_e(10),$o(25000)}',
    'brand/reset'
)

once(
    'className:"min-h-screen bg-[#0e1525] text-white font-sans antialiased selection:bg-[#7ee0a0]/30",children:[',
    'className:"min-h-screen bg-[#0e1525] text-white font-sans antialiased selection:bg-[#7ee0a0]/30","data-calculator":e,"data-theme":e===1?"green":e===2?"blue":"gold",children:[',
    'root data attributes'
)

start = s.index('y("div",{className:"space-y-1.5",children:[p("div",{className:"text-[10px] tracking-[0.14em] text-[#8a96b5]",children:"VEHICLE VARIANT"')
end = s.index('y("div",{className:"space-y-1.5",children:[p("div",{className:"text-[10px] tracking-[0.14em] text-[#8a96b5]",children:"OFFICIAL PROMO DP"', start)
vehicle = '''y("div",{className:"space-y-2.5",children:[p("div",{className:"text-[10px] tracking-[0.14em] text-[#8a96b5]",children:"VEHICLE VARIANT"}),y("div",{className:"bg-[#0f172a] border border-[#2a3655] rounded-[12px] px-3 py-2 flex items-center",children:y("select",{value:brand,onChange:L=>setBrandChoice(L.target.value,L.target.value==="Toyota"?"Vios XLE CVT":null),className:"bg-transparent outline-none w-full text-[16px] font-semibold",children:[p("option",{value:"Mitsubishi",children:"Mitsubishi"}),p("option",{value:"Toyota",children:"Toyota"}),p("option",{value:"Honda",children:"Honda"}),p("option",{value:"Custom",children:"Custom"})]})}),brand==="Toyota"?y("div",{className:"bg-[#0f172a] border border-[#2a3655] rounded-[12px] px-3 py-2 flex items-center",children:y("select",{value:t,onChange:L=>setBrandChoice("Toyota",L.target.value),className:"bg-transparent outline-none w-full text-[16px] font-semibold",children:Object.keys(TM).map(L=>p("option",{value:L,children:L},L))})}):null,brand==="Custom"?y("div",{className:"grid grid-cols-2 gap-2",children:[y("div",{className:"bg-[#0f172a] border border-[#2a3655] rounded-[12px] px-3 py-2",children:p("input",{key:customBrand,defaultValue:customBrand,onBlur:L=>setCustomBrand(L.target.value),onKeyDown:L=>{L.key==="Enter"&&L.currentTarget.blur()},className:"bg-transparent outline-none w-full text-[16px] font-semibold",placeholder:"Brand Name"})}),y("div",{className:"bg-[#0f172a] border border-[#2a3655] rounded-[12px] px-3 py-2",children:p("input",{key:customModel,defaultValue:customModel,onBlur:L=>{setCustomModel(L.target.value),r(L.target.value)},onKeyDown:L=>{L.key==="Enter"&&L.currentTarget.blur()},className:"bg-transparent outline-none w-full text-[16px] font-semibold",placeholder:"Model Name"})})]}):null,p("div",{className:"bg-[#0f172a] border border-[#2a3655] rounded-[12px] px-4 py-3 flex items-center",children:p("input",{key:t,defaultValue:t,onBlur:L=>r(L.target.value),onKeyDown:L=>{L.key==="Enter"&&L.currentTarget.blur()},readOnly:brand==="Toyota",className:"bg-transparent outline-none w-full text-[16px] font-semibold tracking-wide",placeholder:"XPANDER CROSS"})})]}),y("div",{className:"space-y-2",children:[p("div",{className:"flex items-center justify-between gap-3",children:[p("div",{className:"text-[10px] tracking-[0.14em] text-[#8a96b5]",children:"UNIT SRP"}),l>3000000?p("div",{className:"text-[10px] text-[#FFC875]",children:"Custom amount • Slider at max"}):null]}),y("div",{className:"bg-[#0f172a] border border-[#2a3655] rounded-[12px] px-4 py-3 flex items-center justify-between gap-2",children:[p("span",{className:"text-[#8a9b94] text-[16px]",children:"₱"}),p("input",{type:"text",key:l,defaultValue:N(l),onBlur:L=>{let U=L.target.value.replace(/[^0-9.]/g,""),G=Math.min(10000000,parseFloat(U)||0);u(G)},onKeyDown:L=>{L.key==="Enter"&&L.currentTarget.blur()},className:"bg-transparent outline-none w-full text-right font-semibold"})]}),p("input",{type:"range",min:500000,max:3000000,step:10000,value:Math.min(3000000,Math.max(500000,l)),onChange:L=>u(parseFloat(L.target.value)),className:"w-full"}),p("div",{className:"text-[10px] text-[#6B7F78]",children:"Tap number to type • Drag to adjust"})]}),'''
s = s[:start] + vehicle + s[end:]

start = s.index('y("div",{className:"space-y-1.5",children:[p("div",{className:"text-[10px] tracking-[0.14em] text-[#8a96b5]",children:"LOAN TERM"')
end = s.index('y("div",{className:"space-y-2",children:[p("div",{className:"text-[10px] tracking-[0.14em] text-[#8a96b5]",children:"BANK INTEREST RATE (%)"', start)
term = '''y("div",{className:"space-y-2",children:[p("div",{className:"text-[10px] tracking-[0.14em] text-[#8a96b5]",children:"LOAN TERM"}),y("div",{className:"flex items-center gap-2 overflow-x-auto no-scrollbar flex-nowrap",children:[2,3,4,5,6,7].map(L=>p("button",{type:"button",onClick:()=>bf(L),className:`shrink-0 min-w-[68px] h-[40px] rounded-full border text-[13px] font-semibold ${O===L?"bg-white text-black border-white":"bg-[#0f172a] text-white border-[#2a3655]"}`,children:[L,"Y"]},L))})]}),'''
s = s[:start] + term + s[end:]

once('text-[28px] font-black mt-1 tracking-tight','text-[42px] font-black mt-1 tracking-tight','hero size')

inject = r'''<style id="UI-016-V2-PREMIUM">
@import url('https://api.fontshare.com/v2/css?f[]=general-sans@500,600,700&f[]=satoshi@500,600,700,800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@700;800&family=JetBrains+Mono:wght@400;500&family=Inter:wght@600;700&display=swap');
#root>div[data-theme]{width:min(390px,100%);margin:0 auto;min-height:100vh;box-sizing:border-box;border:2px solid var(--ui-accent);border-radius:24px;background:linear-gradient(160deg,var(--ui-bg1),var(--ui-bg2));box-shadow:0 0 0 1px rgba(255,255,255,.08),0 20px 60px rgba(0,0,0,.6),0 8px 24px rgba(0,0,0,.4),inset 0 1px 0 rgba(255,255,255,.08);font-family:'General Sans','Satoshi',Inter,sans-serif}
#root>div[data-theme="green"]{--ui-accent:#A8E6BA;--ui-bg1:#0A1210;--ui-bg2:#0F1E1A;--ui-card:#141E1B;--ui-head:#1A2E26}
#root>div[data-theme="blue"]{--ui-accent:#7AA8FF;--ui-bg1:#080E1A;--ui-bg2:#0F1C30;--ui-card:#131E33;--ui-head:#132040}
#root>div[data-theme="gold"]{--ui-accent:#FFC875;--ui-bg1:#120E07;--ui-bg2:#1E1A0F;--ui-card:#1E1A0F;--ui-head:#2A2212}
#root>div[data-theme] .max-w-\[920px\]{max-width:100%;padding-left:12px;padding-right:12px}
#root>div[data-theme] [class*="bg-[#131c31]"][class*="rounded-[20px]"],#root>div[data-theme] [class*="bg-[#0f172a]"][class*="rounded-[18px]"],#root>div[data-theme] [class*="bg-[#151e32]"][class*="rounded-[18px]"],#root>div[data-theme] [class*="bg-[#0a0f1e]"][class*="rounded-[18px]"]{background:rgba(255,255,255,.06)!important;backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:1px solid color-mix(in srgb,var(--ui-accent) 15%,transparent)!important;border-radius:20px!important;box-shadow:0 8px 32px rgba(0,0,0,.4),0 1px 2px rgba(0,0,0,.5),inset 0 1px 0 rgba(255,255,255,.06)}
#root>div[data-theme] [class*="rounded-[12px]"],#root>div[data-theme] [class*="rounded-xl"],#root>div[data-theme] [class*="rounded-[16px]"]{border-radius:12px!important}
#root>div[data-theme] input:not([type="range"]),#root>div[data-theme] select{font-family:'General Sans','Satoshi',Inter,sans-serif;font-weight:600;font-size:16px;color:#fff;letter-spacing:.3px;-webkit-font-smoothing:antialiased}
#root>div[data-theme] .text-center.font-black.tracking-\[0\.14em\].text-\[16px\]{font-family:'Space Grotesk','Satoshi',sans-serif;font-weight:800;letter-spacing:4px}
#root>div[data-theme] [class*="text-[10px]"]{font-family:'JetBrains Mono','Space Mono',monospace}
#root>div[data-theme] [class*="font-mono"]{font-family:'JetBrains Mono','Space Mono',monospace;font-size:12px;line-height:1.6}
#root>div[data-theme] input[type=range]{-webkit-appearance:none;appearance:none;width:100%;height:4px;background:transparent;border-radius:99px;outline:none}
#root>div[data-theme="green"] input[type=range]{--track:#1E2E28}
#root>div[data-theme="blue"] input[type=range]{--track:#1A2A45}
#root>div[data-theme="gold"] input[type=range]{--track:#2A2212}
#root>div[data-theme] input[type=range]::-webkit-slider-runnable-track{height:4px;background:var(--track);border-radius:99px}
#root>div[data-theme] input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:20px;height:20px;margin-top:-8px;background:#fff;border-radius:50%;box-shadow:0 4px 12px rgba(0,0,0,.3),0 0 12px color-mix(in srgb,var(--ui-accent) 60%,transparent),inset 0 1px 0 rgba(255,255,255,.8);cursor:grab;transition:transform .15s}
#root>div[data-theme] input[type=range]:active::-webkit-slider-thumb{transform:scale(1.2);box-shadow:0 6px 16px rgba(0,0,0,.4),0 0 16px color-mix(in srgb,var(--ui-accent) 80%,transparent)}
#root>div[data-theme] input[type=range]::-moz-range-track{height:4px;background:var(--track);border-radius:99px}
#root>div[data-theme] input[type=range]::-moz-range-thumb{width:20px;height:20px;background:#fff;border:0;border-radius:50%;box-shadow:0 4px 12px rgba(0,0,0,.3);cursor:grab}
#root>div[data-theme] button{font-family:Inter,sans-serif;font-weight:700}
#root>div[data-theme] button[class*="bg-[#86efac]"],#root>div[data-theme] button[class*="bg-[#93c5fd]"],#root>div[data-theme] button[class*="bg-[#fdba74]"]{height:56px;border-radius:100px!important;box-shadow:0 6px 20px color-mix(in srgb,var(--ui-accent) 30%,transparent),0 2px 4px rgba(0,0,0,.3),inset 0 1px 0 rgba(255,255,255,.2)}
#root>div[data-theme] .text-\[12px\].italic{font-style:normal!important}
#root>div[data-theme] [class*="text-[42px]"]{font-family:'General Sans','Satoshi',Inter,sans-serif;font-weight:800}
</style>
<script id="UI-016-V2-BINDER">
(function(){
  function bind(){
    var root=document.querySelector('#root>div[data-calculator]'); if(!root)return;
    var c=root.getAttribute('data-calculator');
    root.setAttribute('data-theme',c==='1'?'green':c==='2'?'blue':'gold');
    root.querySelectorAll('button').forEach(function(b){if(/^COPY DETAILED COMPUTATION$/.test((b.textContent||'').trim()))b.style.color='#000';});
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',bind);else bind();
  new MutationObserver(bind).observe(document.getElementById('root'),{subtree:true,childList:true,attributes:true});
})();
</script>
'''
s = s.replace('</body>', inject + '</body>')

f1 = s[s.index('Ir='):s.index(',ae=', s.index('Ir='))]
cb1 = s[s.index('Go=async'):s.index(',Zf=', s.index('Go=async'))]
if f0 != f1:
    raise SystemExit('FAIL: computation block changed')
if cb0 != cb1:
    raise SystemExit('FAIL: clipboard block changed')

p.write_text(s)
print('UI-016 V2 prepared patch applied:', len(s), 'bytes')
