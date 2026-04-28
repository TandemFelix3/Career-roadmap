import sys
import re

file_path = '/Users/sibi/git-practice/career-roadmap/index.html'
with open(file_path, 'r') as f:
    content = f.read()

# 1. Update default view
content = content.replace(
    "const [activeView, setActiveView] = useState('path_explorer');",
    "const [activeView, setActiveView] = useState('journey');"
)

# 2. Update Sidebar buttons
sidebar_btn_path = """                                            <button onClick={() => setActiveView('path_explorer')} className={`flex items-center gap-3 px-3 py-2 text-left transition-colors border ${activeView === 'path_explorer' ? 'bg-primary text-surface border-primary' : 'text-text border-transparent hover:border-primary'}`}>
                                                <span className="material-symbols-outlined text-[20px]" style={activeView === 'path_explorer' ? {fontVariationSettings: "'FILL' 1"} : {}}>explore</span>
                                                <span className="font-mono text-sm font-medium leading-normal tracking-tight">Path Explorer</span>
                                            </button>"""

new_sidebar_btns = sidebar_btn_path + """
                                            <button onClick={() => setActiveView('explore')} className={`flex items-center gap-3 px-3 py-2 text-left transition-colors border ${activeView === 'explore' ? 'bg-primary text-surface border-primary' : 'text-text border-transparent hover:border-primary'}`}>
                                                <span className="material-symbols-outlined text-[20px]" style={activeView === 'explore' ? {fontVariationSettings: "'FILL' 1"} : {}}>travel_explore</span>
                                                <span className="font-mono text-sm font-medium leading-normal tracking-tight">Explore Roles</span>
                                            </button>
                                            
                                            <button onClick={() => setActiveView('reality_check')} className={`flex items-center gap-3 px-3 py-2 text-left transition-colors border ${activeView === 'reality_check' ? 'bg-primary text-surface border-primary' : 'text-text border-transparent hover:border-primary'}`}>
                                                <span className="material-symbols-outlined text-[20px]" style={activeView === 'reality_check' ? {fontVariationSettings: "'FILL' 1"} : {}}>warning</span>
                                                <span className="font-mono text-sm font-medium leading-normal tracking-tight">Reality Check</span>
                                            </button>"""

content = content.replace(sidebar_btn_path, new_sidebar_btns)

# 3. Add components to App
app_components = """                    {activeView === 'path_explorer' && <PathExplorer setActiveView={(view) => { setActiveView(view); setIsMobileMenuOpen(false); }} setActiveTrackId={(id) => { setActiveTrackId(id); setIsMobileMenuOpen(false); }} />}"""
new_app_components = app_components + """
                    {activeView === 'explore' && <ExploreRoles />}
                    {activeView === 'reality_check' && <RealityCheck />}"""

content = content.replace(app_components, new_app_components)

# 4. Add ExploreRoles and RealityCheck components before App definition
new_components = """        const ExploreRoles = () => {
            const roles = [
                { cat: 'Product', title: 'Product Specialist', tier: 'Tier 1', desc: 'Owns product workflows, customer feedback synthesis, and cross-functional coordination.', salary: '₹8–14 LPA', prep: '4–8 weeks', targets: 'Freshworks, Zoho, Chargebee, Postman, Atlan' },
                { cat: 'Product', title: 'Product Operations', tier: 'Tier 1', desc: 'The "make the product team work better" role. Tools, processes, feedback systems, metrics infrastructure.', salary: '₹10–16 LPA', prep: '2–3 months', targets: 'Razorpay, CRED, Postman, Atlassian, Atlan' },
                { cat: 'Product', title: 'Associate Product Manager', tier: 'Tier 2', desc: 'Structured rotational programs designed for non-traditional backgrounds.', salary: '₹15–25 LPA', prep: '3–6 months', targets: 'Google, Atlassian, Microsoft, Razorpay, Atlan' },
                { cat: 'Product', title: 'AI Product Manager', tier: 'Tier 2', desc: 'Focused on LLM-powered features, evals, and agentic systems.', salary: '₹19–37 LPA', prep: '3–4 months', targets: 'Atlan, Glean, Sarvam AI, Krutrim' },
                { cat: 'Product', title: 'Product Marketing Manager', tier: 'Tier 2', desc: 'Owns positioning, launches, competitive intel, customer narratives.', salary: '₹10–18 LPA', prep: '3–4 months', targets: 'Postman, Freshworks, Chargebee, Zoho' },
                { cat: 'Technical', title: 'Product Engineer', tier: 'Tier 3', desc: 'Engineers who think in product, ship fast, and own outcomes.', salary: '₹15–35 LPA', prep: '6–9 months', targets: 'Linear, Vercel, Razorpay, Zerodha' },
                { cat: 'Technical', title: 'Design Engineer', tier: 'Tier 2/3', desc: 'Sits between design and frontend code. High design bar.', salary: '₹12–28 LPA', prep: '5–7 months', targets: 'Razorpay, CRED, Postman, HackerRank' },
            ];

            return (
                <div className="flex-1 flex flex-col h-full bg-background overflow-hidden">
                    <header className="h-auto md:h-16 border-b border-primary bg-surface shrink-0 flex items-center p-4 md:px-6 z-10 sticky top-0">
                        <h1 className="text-3xl font-heading font-bold tracking-tight text-primary">Explore Roles</h1>
                    </header>
                    <main className="flex-1 overflow-y-auto p-6 md:p-10 custom-scrollbar flex flex-col gap-8">
                        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
                            {roles.map(r => (
                                <article key={r.title} className="bg-surface border border-primary p-6 shadow-brutal shadow-color-primary flex flex-col gap-4 group hover:-translate-y-1 transition-transform">
                                    <div className="flex justify-between items-start">
                                        <span className="font-mono text-[10px] uppercase tracking-widest text-accent bg-accent/10 px-2 py-1 border border-accent/30">{r.cat}</span>
                                        <span className="font-mono text-[10px] uppercase tracking-widest text-muted">{r.tier}</span>
                                    </div>
                                    <h3 className="font-heading text-xl font-bold text-primary leading-tight">{r.title}</h3>
                                    <p className="font-body text-sm text-text leading-relaxed">{r.desc}</p>
                                    <div className="mt-auto pt-4 flex flex-col gap-2 border-t border-primary/20 font-mono text-[11px]">
                                        <div className="flex justify-between"><span className="text-muted uppercase">Salary</span><span className="font-bold text-primary">{r.salary}</span></div>
                                        <div className="flex justify-between"><span className="text-muted uppercase">Prep Time</span><span className="font-bold text-primary">{r.prep}</span></div>
                                        <div className="flex flex-col mt-2 pt-2 border-t border-primary/10 gap-1">
                                            <span className="text-muted uppercase">Target Companies</span>
                                            <span className="text-primary truncate">{r.targets}</span>
                                        </div>
                                    </div>
                                </article>
                            ))}
                        </div>
                    </main>
                </div>
            );
        };

        const RealityCheck = () => {
            return (
                <div className="flex-1 flex flex-col h-full bg-background overflow-hidden">
                    <header className="h-auto md:h-16 border-b border-primary bg-surface shrink-0 flex items-center p-4 md:px-6 z-10 sticky top-0">
                        <h1 className="text-3xl font-heading font-bold tracking-tight text-primary flex items-center gap-3">
                            <span className="material-symbols-outlined text-[32px] text-accent">warning</span>
                            Reality Check
                        </h1>
                    </header>
                    <main className="flex-1 overflow-y-auto p-6 md:p-12 custom-scrollbar bg-primary text-surface">
                        <div className="max-w-3xl mx-auto flex flex-col gap-12 py-8">
                            
                            <section className="border-l-4 border-accent pl-6">
                                <h2 className="font-heading text-3xl font-bold mb-4 uppercase tracking-tight text-surface">On "Managerial"</h2>
                                <p className="font-body text-lg leading-relaxed text-surface/90">
                                    The "managerial" label can mean very different things. Most roles on this list are individual contributor (IC) roles with cross-functional ownership. Genuine people-management roles in tech almost always require 4+ years of IC experience first. Your "ownership and leading initiatives" instinct is what hiring managers in IC product roles want; explicit people-management is a 3+ year goal.
                                </p>
                            </section>

                            <section className="border-l-4 border-accent pl-6">
                                <h2 className="font-heading text-3xl font-bold mb-4 uppercase tracking-tight text-surface">On "Less Customer-Facing"</h2>
                                <p className="font-body text-lg leading-relaxed text-surface/90">
                                    A few of the roles (Product Specialist, DevRel) still involve some user interaction — but the relationship is different from support. You're shaping the product they use, not unblocking their tickets. If "no customer interaction at all" is a hard constraint, prioritize: Product Analyst, Product Engineer, AI Engineer, Technical Writer. These are genuinely behind-the-scenes.
                                </p>
                            </section>

                            <section className="border-l-4 border-accent pl-6">
                                <h2 className="font-heading text-3xl font-bold mb-4 uppercase tracking-tight text-surface">On AI-Related FOMO</h2>
                                <p className="font-body text-lg leading-relaxed text-surface/90">
                                    AI roles pay well right now and the field is genuinely exciting. But picking AI because it's hot, when your underlying interest is in building products generally, is a recipe for two years of feeling lost. The right framing is: AI as the layer you operate within, while doing whatever core craft (product, design, analytics, engineering) actually pulls you. That layered framing ages well; chasing the buzzword does not.
                                </p>
                            </section>
                            
                        </div>
                    </main>
                </div>
            );
        };

        const App = () => {"""

content = content.replace("        const App = () => {", new_components)

with open(file_path, 'w') as f:
    f.write(content)

print("Added sections successfully.")
