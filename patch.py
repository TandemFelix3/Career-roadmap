import sys

file_path = '/Users/sibi/git-practice/career_roadmap_app.html'
with open(file_path, 'r') as f:
    content = f.read()

# Replace App component
target_app = """        const App = () => {
            const [activeView, setActiveView] = useState('path_explorer'); // Default to Path Explorer for testing
            const [activeTrackId, setActiveTrackId] = useState(tracks[0].id);
            const activeTrack = tracks.find(t => t.id === activeTrackId);
            const [isChecklistOpen, setIsChecklistOpen] = useState(false);

            return (
                <div className="flex w-full h-full">
                    <Sidebar 
                        activeView={activeView}
                        setActiveView={setActiveView}
                        activeTrackId={activeTrackId} 
                        setActiveTrackId={setActiveTrackId} 
                        setIsChecklistOpen={setIsChecklistOpen}
                    />
                    {activeView === 'journey' && (
                        <main className="flex-1 flex overflow-hidden">
                            <Intro track={activeTrack} />
                            <Timeline track={activeTrack} />
                        </main>
                    )}
                    {activeView === 'app_hub' && <ApplicationHub />}
                    {activeView === 'path_explorer' && <PathExplorer setActiveView={setActiveView} setActiveTrackId={setActiveTrackId} />}
                    {isChecklistOpen && <ChecklistModal onClose={() => setIsChecklistOpen(false)} />}
                </div>
            );
        };"""

replacement_app = """        const App = () => {
            const [activeView, setActiveView] = useState('path_explorer'); // Default to Path Explorer for testing
            const [activeTrackId, setActiveTrackId] = useState(tracks[0].id);
            const activeTrack = tracks.find(t => t.id === activeTrackId);
            const [isChecklistOpen, setIsChecklistOpen] = useState(false);
            const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

            return (
                <div className="flex flex-col md:flex-row w-full h-full overflow-hidden">
                    {/* Mobile Header */}
                    <div className="md:hidden flex items-center justify-between p-4 bg-surface border-b border-primary z-20 shrink-0">
                        <h1 className="text-primary font-heading text-xl font-semibold">Sibi's Roadmap</h1>
                        <button onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)} className="p-2 border border-transparent hover:border-primary transition-colors flex">
                            <span className="material-symbols-outlined">{isMobileMenuOpen ? 'close' : 'menu'}</span>
                        </button>
                    </div>

                    <div className={`fixed inset-y-0 left-0 transform ${isMobileMenuOpen ? 'translate-x-0' : '-translate-x-full'} md:relative md:translate-x-0 transition duration-200 ease-in-out z-30 md:z-auto bg-background md:bg-transparent h-full shadow-2xl md:shadow-none w-64 shrink-0`}>
                        <Sidebar 
                            activeView={activeView}
                            setActiveView={(view) => { setActiveView(view); setIsMobileMenuOpen(false); }}
                            activeTrackId={activeTrackId} 
                            setActiveTrackId={(id) => { setActiveTrackId(id); setIsMobileMenuOpen(false); }} 
                            setIsChecklistOpen={setIsChecklistOpen}
                        />
                    </div>
                    {isMobileMenuOpen && <div className="fixed inset-0 bg-primary/40 z-20 md:hidden" onClick={() => setIsMobileMenuOpen(false)}></div>}

                    {activeView === 'journey' && (
                        <main className="flex-1 flex flex-col md:flex-row overflow-hidden md:overflow-hidden h-full overflow-y-auto md:overflow-y-visible">
                            <Intro track={activeTrack} />
                            <Timeline track={activeTrack} />
                        </main>
                    )}
                    {activeView === 'app_hub' && <ApplicationHub />}
                    {activeView === 'path_explorer' && <PathExplorer setActiveView={(view) => { setActiveView(view); setIsMobileMenuOpen(false); }} setActiveTrackId={(id) => { setActiveTrackId(id); setIsMobileMenuOpen(false); }} />}
                    {isChecklistOpen && <ChecklistModal onClose={() => setIsChecklistOpen(false)} />}
                </div>
            );
        };"""

content = content.replace(target_app, replacement_app)

# Replace Intro
content = content.replace(
    '<section className="w-2/5 p-16 flex flex-col h-full overflow-y-auto custom-scrollbar bg-background border-r border-primary">',
    '<section className="w-full md:w-2/5 p-8 md:p-16 flex flex-col h-auto md:h-full md:overflow-y-auto custom-scrollbar bg-background border-b md:border-b-0 md:border-r border-primary shrink-0">'
)

# Replace Timeline
content = content.replace(
    '<section className="w-3/5 relative h-full overflow-y-auto custom-scrollbar bg-background p-16">',
    '<section className="w-full md:w-3/5 relative h-full flex-1 overflow-y-auto md:overflow-y-auto custom-scrollbar bg-background p-8 md:p-16 pt-12 md:pt-16">'
)

# Replace AppHub Header
content = content.replace(
    '<header className="h-16 border-b border-primary bg-surface shrink-0 flex items-center justify-between px-6 z-10 sticky top-0">',
    '<header className="h-auto md:h-16 border-b border-primary bg-surface shrink-0 flex flex-col md:flex-row md:items-center justify-between p-4 md:px-6 z-10 sticky top-0 gap-4 md:gap-0">'
)
content = content.replace(
    '<div className="flex items-center gap-6">',
    '<div className="flex items-center gap-6 justify-between md:justify-start w-full md:w-auto">'
)

# Replace AppHub Column
content = content.replace(
    'className="flex-none w-[32vw] min-w-[340px] max-w-[450px] flex flex-col h-full"',
    'className="flex-none w-[85vw] md:w-[32vw] min-w-[300px] md:min-w-[340px] max-w-[450px] flex flex-col h-full"'
)

# Replace PathExplorer main and section
content = content.replace(
    '<main className="flex-1 flex overflow-y-auto custom-scrollbar">',
    '<main className="flex-1 flex flex-col md:flex-row overflow-y-auto custom-scrollbar">'
)

content = content.replace(
    'className={`flex-1 flex flex-col h-full border-r border-primary pt-10 pb-12 px-8 xl:px-12 relative group transition-all duration-300 hover:bg-surface ${isDimmed ? \'opacity-30 grayscale hover:opacity-100 hover:grayscale-0\' : \'opacity-100\'}`}>',
    'className={`w-full md:flex-1 flex flex-col h-auto md:h-full border-b md:border-b-0 md:border-r border-primary pt-10 pb-12 px-8 xl:px-12 relative group transition-all duration-300 hover:bg-surface ${isDimmed ? \'opacity-30 grayscale hover:opacity-100 hover:grayscale-0\' : \'opacity-100\'}`}>'
)

with open(file_path, 'w') as f:
    f.write(content)

print("Replacement done.")
