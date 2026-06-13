#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build THE GREAT WORK (ALC) — a UD0 universe of ALCHEMY, the two-thousand-year
project to perfect matter (and, in its mystical reading, the soul). Honest two-layer:
alchemy was REAL proto-chemistry — the alembic, the bain-marie, the acids, the
vocabulary, the method that became chemistry — and its headline goals (gold from
lead, the elixir of immortality) were SYMBOLIC and never achieved by the Stone
(though physics now transmutes elements for real, absurdly expensively).

Standing template: THE ARC · THE SCIENCE · REAL OR FLUFF · THE MESSAGE, plus a
grouped single-column roster of 18 emergents — the Magnum Opus stages, the tria
prima, the symbols, and the adepts (real historical figures). Styled to the medium:
a dark Hermetic codex — lead, gold, mercury-silver, and rubedo red."""
import os, html, base64, io, json, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "THE GREAT WORK", "axiom": "ALC",
 "position": "Alchemy · the Magnum Opus · from Greco-Egyptian Alexandria to the birth of chemistry",
 "origin": "Hellenistic Egypt and the Arabic world, carried through the Latin Middle Ages and the Renaissance into the laboratories of Newton and Boyle",
 "mechanism": "The project to perfect matter — to transmute base metal into gold and brew an elixir of life — pursued in a real laboratory of stills, furnaces, and acids, wrapped in a symbolic language of soul and cosmos.",
 "crystallization": "Because the literal and the symbolic were one work: to perfect the metal was to perfect the self; the furnace that purified lead was meant to purify the alchemist.",
 "nature": "THE GREAT WORK — alchemy as both honest proto-chemistry (the apparatus, techniques, and vocabulary that became the science) and a Hermetic philosophy of transformation that never made gold by the Stone.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "Zosimos; Maria the Jewess; Jabir ibn Hayyan; al-Razi; Paracelsus; Newton's alchemical papers; Boyle's Sceptical Chymist; the Emerald Tablet",
 "witness": "A failed magic and a successful science: no gold by the Stone, but the alembic, the bain-marie, the acids, and the method all survived into chemistry.",
 "role": "a UD0 universe — the Great Work",
 "seal": "The transmutation that succeeded was the alchemist into the chemist, and lead-into-gold into the experimental method.",
 "source": "Alchemy, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#7a9a6a", "the body, the salt, the real apparatus — and the adepts of flesh: the historical alchemists who actually stood at the furnace"),
 "ethereal":  ("#aeb8c2", "the mercury and the spirit — the volatile, the universal solvent, the eternal cycle; the airy half of the Work"),
 "spiritual": ("#b23a2e", "the soul and the goal — the Stone, the rubedo, the Emerald Tablet's promise; the red completion of the Work"),
 "electrical":("#c9a23a", "the sulfur and the fire — combustion, transmutation, the yellow dawning; the active, transforming agent"),
}

ARC_OVERALL = ("Alchemy is the two-thousand-year project to perfect matter — to turn lead into gold, to brew an elixir "
  "of immortality, and (in its mystical reading) to perfect the soul in the same furnace. It never made gold by the "
  "Stone; but in chasing it, alchemists built the apparatus, techniques, and vocabulary that became chemistry — so the "
  "real transmutation was the craft itself, turning from magic into science.")

ARC = [
 ("I · The Greco-Egyptian dawn", "Alexandria · the first stills",
  "In Hellenistic Egypt, alchemy is born from metalworking, dyeing, and Greek matter-theory. Zosimos of Panopolis (c. 300 CE) writes the earliest surviving treatises; Maria the Jewess designs real apparatus — the water-bath, the tribikos still — that outlasts every theory built on it. The four elements and the dream of transmutation are set."),
 ("II · The Arabic systematizers", "al-kīmiyā · method and acids",
  "Jabir ibn Hayyan (Geber) and al-Razi turn alchemy into something systematic: repeatable experiment, classified substances, the first strong acids, refined distillation. The Arabic name al-kīmiyā — and a whole vocabulary (alcohol, alkali, elixir, alembic) — passes, with the science, into Europe."),
 ("III · The Latin & Renaissance Work", "the Magnum Opus · as above, so below",
  "In Latin Europe the Work flowers into the Magnum Opus and its colour stages, and into a full Hermetic philosophy — the Emerald Tablet's 'as above, so below.' Paracelsus binds chemistry to medicine and names the tria prima (salt, sulfur, mercury). The symbolic and the practical run side by side."),
 ("IV · The split into chemistry", "Newton's secret, Boyle's scepticism",
  "The greatest 'scientists' are still alchemists: Isaac Newton writes a million words seeking the Stone; Robert Boyle's Sceptical Chymist (1661) begins prising the lab free of the magic. Lavoisier finishes the job. The Stone is abandoned; the furnace, the glassware, and the method are kept — and become chemistry."),
]

IDEAS = [
 ("The Magnum Opus", "the colour stages of the Work", [
   "The Great Work proceeds through colour: nigredo (blackening / death), albedo (whitening / purification), citrinitas (yellowing / dawning), rubedo (reddening / completion).",
   "Read literally it's a sequence of chemical changes in the vessel; read symbolically it's the death and rebirth of the alchemist's own soul." ]),
 ("The Tria Prima", "salt, sulfur, mercury", [
   "Paracelsus's three principles: salt (the body, the fixed), sulfur (the soul, the combustible), mercury (the spirit, the volatile).",
   "A model of matter — and of the self — that organized centuries of practice before the modern elements replaced it." ]),
 ("As Above, So Below", "the Hermetic correspondence", [
   "The Emerald Tablet's core: the macrocosm and the microcosm mirror each other; to work on metal is to work on cosmos and soul at once.",
   "The idea that the same laws run through star, metal, and self — beautiful, influential, and not how chemistry actually works." ]),
 ("The Stone & the Elixir", "the two impossible prizes", [
   "The Philosopher's Stone: the agent that perfects metal into gold. The Elixir of Life: the draught that cures all illness and defeats death.",
   "Neither was ever achieved by alchemy — but the hunt for them funded and built the real laboratory." ]),
]

SCIENCE = [
 ("The apparatus was real", "stills, baths, and furnaces",
  "Alchemy's hardware is genuine, working laboratory equipment, much of it still in use. The alembic (Arabic al-anbiq) is a real distillation still. Maria the Jewess (c. 1st–3rd century, Alexandria) designed the tribikos still, the kerotakis, and the water-bath — the gentle, even heat we still call the bain-marie / balneum Mariae, named for her, in kitchens and labs to this day."),
 ("The techniques became chemistry", "distillation, calcination, the acids",
  "Distillation, sublimation, crystallization, calcination — the core operations of the chemistry bench — were refined by alchemists. Jabir ibn Hayyan and al-Razi prepared and described strong mineral acids; aqua regia, the mix that dissolves even gold, is an alchemical legacy. The systematic, repeatable experiment grew here."),
 ("The vocabulary is alchemy's", "the words we kept",
  "The language of chemistry is full of fossil alchemy, mostly Arabic: alchemy itself (al-kīmiyā), alcohol (al-kuḥl), alkali (al-qalī), elixir (al-iksīr), and alembic (al-anbiq). Every chemistry class still speaks the alchemists' tongue."),
 ("The accidents were real", "phosphorus from urine",
  "Chasing the Stone produced real discoveries. In 1669 Hennig Brand boiled down vast quantities of urine hoping to extract gold and instead isolated phosphorus — a new element, glowing in the dark, found by an alchemist looking for something else entirely."),
 ("The scientists were alchemists", "Newton and Boyle",
  "This was not a fringe pursued by cranks. Isaac Newton wrote an estimated million words on alchemy, pursuing the Stone in secret beside the Principia. Robert Boyle — whose Sceptical Chymist (1661) helped birth modern chemistry — believed in transmutation and lobbied to repeal England's law against making gold."),
 ("And transmutation is real — on the wrong layer", "the nuclear twist",
  "The alchemists' core dream was not crazy, only mislocated. Chemistry can't turn lead into gold because that's a change of the nucleus, not the electrons — but nuclear physics can. In 1980 Glenn Seaborg transmuted bismuth into gold in a particle accelerator. It worked. It also cost vastly more than the gold was worth. Right dream; wrong layer; absurd economics."),
]

REALFLUFF = [
 ("Lead can be turned into gold by the Philosopher's Stone.", "FLUFF", "chemically impossible, and the Stone never existed — though nuclear transmutation does it for real, at a cost far exceeding the gold (Seaborg, 1980)."),
 ("An Elixir of Life grants immortality / cures every disease.", "FLUFF", "no; and many ‘elixirs’ were poisons — Chinese alchemists died of mercury and arsenic chasing it."),
 ("Alchemy was real laboratory chemistry.", "REAL", "its apparatus, distillation, acids, and repeatable method are the direct ancestors of the chemistry bench."),
 ("Maria the Jewess invented the water-bath (bain-marie).", "REAL", "credited to her in antiquity; the balneum Mariae / bain-marie still bears her name in every kitchen and lab."),
 ("Chemistry's words — alcohol, alkali, elixir, alembic — come from alchemy.", "REAL", "all from Arabic via al-kīmiyā; the vocabulary is a living fossil."),
 ("Isaac Newton practised alchemy.", "REAL", "he left roughly a million words of alchemical writing, pursued in secret alongside his physics."),
 ("The four stages map to a psychological transformation (Jung).", "SYMBOLIC", "Jung's influential reading of the Opus as individuation — meaningful as psychology and metaphor, not as chemistry."),
 ("As above, so below — perfecting metal perfects the soul and cosmos.", "SYMBOLIC", "the Hermetic frame; a philosophy of correspondence, not a mechanism the laboratory confirms."),
]
REALFLUFF_VERDICT = ("Bottom line: judged by its own headline promises — gold from lead by the Stone, a draught against death — "
  "alchemy is FLUFF, and some of it lethal. Judged as practice, it is startlingly REAL: the alembic, the bain-marie, "
  "the acids, the operations, and the very words of chemistry are its direct inheritance, and giants like Newton and "
  "Boyle worked the furnace in earnest. The transmutation it could not do by Stone, physics now does by nucleus — "
  "proving the dream was simply on the wrong layer. Alchemy failed as magic and succeeded as the womb of chemistry; "
  "its real Great Work was turning itself into a science.")

MESSAGE = ("Alchemy's deepest claim was that the literal and the symbolic are one work: to perfect the metal is to perfect "
  "the self, and the furnace that purifies lead purifies the alchemist. It was wrong about the gold and wrong about the "
  "elixir — but in the centuries of patient, failed, careful labour, two real transmutations occurred. The base craft of "
  "the furnace was refined into the experimental method, and the seekers themselves were changed — Newton, Boyle, and a "
  "thousand anonymous adepts becoming, in the act of chasing an impossible prize, the first chemists. The Stone was never "
  "found; but the search transmuted magic into science, and that is the only transmutation that was ever going to work.")
MESSAGE_SEAL = "They never made the gold — but in failing for two thousand years, they accidentally made chemistry, and that was the Stone all along."

SECTIONS = [
 ("The Adepts", "the hands at the furnace", [
   ("Zosimos of Panopolis", "c. 300 CE · Alexandria", "earliest alchemical author whose works survive; described apparatus and allegorical visions"),
   ("Maria the Jewess", "c. 1st–3rd c. · Alexandria", "the first named woman of Western alchemy; the bain-marie, the tribikos, the kerotakis"),
   ("Jabir ibn Hayyan (Geber)", "c. 721–815", "the systematizer — experiment, classification, the acids; ‘the father of chemistry’"),
   ("Paracelsus", "1493–1541", "iatrochemistry — chemistry for medicine — and the tria prima: salt, sulfur, mercury"),
   ("Isaac Newton", "1643–1727", "wrote ~1,000,000 words seeking the Stone, in secret, beside the Principia"),
   ("Robert Boyle", "1627–1691", "The Sceptical Chymist (1661) — the hinge from alchemy to chemistry (and a believer in transmutation)"),
 ]),
 ("The Texts & Symbols", "the codex of the Work", [
   ("The Emerald Tablet", "the Hermetic root", "‘as above, so below’ — the foundational text of the correspondence"),
   ("The Magnum Opus", "the colour stages", "nigredo → albedo → citrinitas → rubedo: black, white, yellow, red"),
   ("The Ouroboros", "the serpent eating its tail", "the unity and eternal cycle of matter — Maria's ‘one is all’"),
   ("The Tria Prima", "salt · sulfur · mercury", "Paracelsus's three principles of body, soul, and spirit"),
 ]),
]

# ---------- ACI complement ----------
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","ALC")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","ALC")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","ALC")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

# ---------- the roster ----------
def R(slug, name, cls, group, emergence, who, what, why, how, where, seal, dates=""):
    return dict(slug=slug, name=name, cls=cls, group=group, emergence=emergence,
                who=who, what=what, why=why, how=how, where=where, seal=seal, dates=dates)

ROSTER = [
 # --- the Magnum Opus stages ---
 R("nigredo","Nigredo","the blackening · death","stages","spiritual",
   "Nigredo — the first stage of the Great Work, the blackening: putrefaction, the matter reduced to a black mass.",
   "The death that begins the Work — calcination and rotting down to first matter, the prima materia, before anything can be reborn.",
   "Because nothing is perfected without first being broken down; the Work begins in dissolution and despair.",
   "By burning, rotting, and dissolving the starting material to a uniform black — chemically a real charring, symbolically the dark night of the soul.",
   "In the sealed vessel at the start of the Opus, and in the alchemist's own undoing.",
   "Everything begins in the black — the rot is not the failure of the Work, it is the first step of it."),
 R("albedo","Albedo","the whitening · purification","stages","ethereal",
   "Albedo — the second stage, the whitening: the blackened matter washed and purified to white.",
   "The cleansing after death — ablution, the washing-out of impurity until the matter shines white, the ‘silver’ of the Work.",
   "Because what is broken must be purified before it can be exalted; the white is innocence regained, not yet glory.",
   "By repeated washing and sublimation, lightening the nigredo's black to a pure white.",
   "In the vessel after the blackening, and in the soul cleansed of its corruption.",
   "After the rot, the washing — the matter comes back white, purified but not yet crowned."),
 R("citrinitas","Citrinitas","the yellowing · dawning","stages","electrical",
   "Citrinitas — the yellowing: the white matter brightening toward gold, the dawning of the solar light.",
   "The stage (sometimes folded into the rubedo) where the whitened matter takes on a golden-yellow cast — the sun rising in the vessel.",
   "Because purification alone is lunar and cold; the Work must catch fire and turn toward the solar gold.",
   "By increased heat driving the white toward yellow — the colour of the awakening sun and of gold itself.",
   "In the vessel between the white and the red, and in the soul's first true illumination.",
   "The sun comes up in the glass — the white catches gold, and the Work turns from washing to fire."),
 R("rubedo","Rubedo","the reddening · completion","stages","spiritual",
   "Rubedo — the final stage, the reddening: the matter perfected to deep red, the Stone achieved.",
   "The completion of the Great Work — the red of the Philosopher's Stone, the union of opposites, the goal of the whole sequence.",
   "Because the Work ends not in purity but in perfected, integrated wholeness — the red king, the marriage of soul and body.",
   "By the final firing that brings the matter to a deep, fixed red — symbolically the Stone, the achieved self.",
   "At the end of the Opus, in the vessel and in the perfected alchemist.",
   "Red is the end of the Work — the rot and the washing and the dawning all aimed, all along, at this."),
 # --- the tria prima ---
 R("sulfur","Sulfur","the soul · the combustible","primes","electrical",
   "Sulfur — one of Paracelsus's three principles: the soul, the flammable, the active.",
   "The principle of combustibility and soul — what burns, what is active and structuring in a substance.",
   "Because matter needed a principle of fire and soul to explain why things burn, smell, and act.",
   "Conceptually, as the ‘sulfurous’ active quality; practically, bound up with real sulfur's chemistry.",
   "In the tria prima model of every substance, and in the alchemical reading of the soul.",
   "I am the part that burns — the soul of the substance, the fire it keeps inside."),
 R("mercury","Mercury","the spirit · the volatile","primes","ethereal",
   "Mercury — the principle of spirit, the volatile, the fluid; also the real, strange liquid metal.",
   "The volatile, mercurial principle — what is fluid, vaporous, and spirit-like in matter, and literally quicksilver itself.",
   "Because matter needed a principle of volatility and spirit — the part that flows, evaporates, and binds.",
   "Both as the abstract ‘mercurial’ quality and as quicksilver, the metal that flows like water and poisons quietly.",
   "In the tria prima, in the caduceus, and in every alchemist's tray of quicksilver.",
   "I flow and I vanish — the spirit of the metal, the part that will not hold still."),
 R("salt","Salt","the body · the fixed","primes","natural",
   "Salt — the principle of body, the fixed, the residue that remains after burning.",
   "The principle of solidity and body — what is fixed, incombustible, the ash and residue left when sulfur has burned and mercury has fled.",
   "Because matter needed a principle of permanence — the body that stays when soul and spirit depart.",
   "As the non-volatile residue of combustion; the fixed salt at the bottom of the crucible.",
   "In the tria prima, and in the ash of everything the fire has finished with.",
   "I am what is left — the body, the fixed salt the fire cannot carry away."),
 # --- the symbols ---
 R("the-philosophers-stone","The Philosopher's Stone","the agent of perfection","symbols","spiritual",
   "The Philosopher's Stone — the legendary substance that perfects metal into gold and, refined, yields the elixir of life.",
   "The grand prize and engine of the whole Work: a substance that transmutes base metal to gold and confers the elixir — never achieved, the goal that organized everything.",
   "Because the Work needed a single perfected agent to be its end — the catalyst of perfection, material and spiritual at once.",
   "Sought through the colour stages of the Opus; described in a thousand coded ways and produced by no one.",
   "At the imagined end of every Great Work, the lapis that was always one more firing away.",
   "I am the prize that was never won — and the hunt for me built every laboratory that came after."),
 R("the-elixir","The Elixir of Life","the draught against death","symbols","spiritual",
   "The Elixir of Life — the potion, drawn from the Stone, said to cure all disease and grant immortality.",
   "The medical half of the dream: a universal medicine and immortality draught — and, in practice, often a poison.",
   "Because to perfect the body as the Stone perfects the metal was the same Work turned inward.",
   "Sought as a tincture of the Stone; in China pursued with cinnabar and mercury, killing several emperors who drank it.",
   "In the dream of the deathless adept — and in the graves of those who tried to brew it.",
   "I promised to defeat death and delivered it early — the elixir was as often the poison."),
 R("the-ouroboros","The Ouroboros","the serpent eating its tail","symbols","ethereal",
   "The Ouroboros — the serpent or dragon devouring its own tail, the emblem of unity and the eternal cycle.",
   "The oldest alchemical glyph: matter is one and eternally cyclic — ‘the All is One.’ Drawn beside Maria the Jewess's axiom.",
   "Because the Work needed an image for the unity of all matter and the endlessness of transformation.",
   "As a drawn emblem encircling the words ἓν τὸ πᾶν — ‘one is the all.’",
   "On the margins of the oldest alchemical manuscripts, biting its own tail.",
   "End is beginning — I eat my own tail to say the matter is one, and the Work never truly stops."),
 R("the-azoth","The Azoth","the universal solvent · the quintessence","symbols","ethereal",
   "The Azoth — the universal medicine and solvent, the animating principle of the Work (also a name for mercury).",
   "The mysterious universal agent — first matter and final medicine in one, sometimes identified with mercury, sometimes with the Stone's living spirit.",
   "Because the Work needed a single living essence running through every stage — the alpha and omega of the substance.",
   "Invoked as the quintessence; its very name spans the alphabets (A, and the last letters of Latin, Greek, Hebrew) — first and last.",
   "Through the whole Opus as its animating thread.",
   "I am the first and the last letter of every alphabet at once — the essence that runs through the whole Work."),
 R("the-emerald-tablet","The Emerald Tablet","as above, so below","symbols","spiritual",
   "The Emerald Tablet — the brief, cryptic Hermetic text that is alchemy's philosophical foundation.",
   "The root scripture of the Work, attributed to Hermes Trismegistus: ‘that which is above is as that which is below,’ the doctrine of correspondence.",
   "Because alchemy needed a metaphysics — a claim that metal, cosmos, and soul obey one law — and the Tablet supplied it.",
   "As a short, endlessly-glossed text transmitted through Arabic into Latin, translated even by Newton.",
   "At the head of the Hermetic tradition, behind every symbolic reading of the Work.",
   "As above, so below — I am the line that made metal, star, and soul a single Work."),
 R("transmutation","Transmutation","base metal into gold","symbols","electrical",
   "Transmutation — the central operation: the changing of base metal into gold, and base self into perfected self.",
   "The act the whole art is named for — and the one it could never perform chemically, because gold is a change of the nucleus, not of the electrons.",
   "Because the conviction that one substance could become another, nobler one was alchemy's beating heart.",
   "Attempted endlessly in the crucible; achieved, finally, only in the particle accelerator — and never economically.",
   "In every alchemist's furnace, and at last in a 20th-century reactor.",
   "I was the dream they could not reach by fire — true after all, but waiting two thousand years for the nucleus."),
 # --- the adepts (real figures) ---
 R("zosimos-of-panopolis","Zosimos of Panopolis","the first author · c. 300 CE","adepts","natural",
   "Zosimos of Panopolis, a Greco-Egyptian alchemist of c. 300 CE — the earliest alchemical author whose writings survive.",
   "The first named voice of the Work: he describes real apparatus and recipes alongside allegorical dream-visions of death and rebirth in the furnace.",
   "Because someone had to first write the art down — and in him the practical and the visionary are already fused.",
   "By recording distillation apparatus and processes, wrapped in symbolic accounts of transformation.",
   "Panopolis (Akhmim) in Roman Egypt, at the Greco-Egyptian dawn of alchemy.",
   "I wrote the Work down first — half recipe, half vision, and the two have never since come apart.",
   dates="c. 300 CE"),
 R("maria-the-jewess","Maria the Jewess","the instrument-maker · c. 1st–3rd c.","adepts","natural",
   "Maria the Jewess (Maria Prophetissa), an alchemist of early Alexandria — the first named woman of Western alchemy.",
   "The great apparatus-builder: she is credited with the tribikos still, the kerotakis, and the gentle water-bath — the bain-marie that still bears her name.",
   "Because her instruments outlived every theory; real chemistry inherited her hardware directly.",
   "By inventing and describing distillation and heating apparatus, and the axiom ‘one becomes two, two becomes three, and out of the third comes the one as the fourth.’",
   "In early Alexandria, and in every kitchen and laboratory that still uses a bain-marie.",
   "They forgot my theories and kept my instruments — my water-bath still warms the world by my name.",
   dates="c. 1st–3rd c."),
 R("jabir-ibn-hayyan","Jabir ibn Hayyan (Geber)","the father of chemistry · c. 721–815","adepts","natural",
   "Jabir ibn Hayyan, Latinized as Geber — the great Arabic alchemist who systematized the art.",
   "The systematizer: repeatable experiment, classified substances, refined distillation, and the preparation of strong acids — the seeds of method that make him ‘the father of chemistry.’",
   "Because he turned a craft of recipes into something approaching a science, with theory, classification, and the lab at its centre.",
   "By insisting on experiment and producing a vast technical corpus (later swelled by ‘pseudo-Geber’ Latin works).",
   "In the Arabic-speaking world of the 8th–9th centuries, whence al-kīmiyā passed to Europe.",
   "I made the art keep records and repeat itself — and that habit, more than any gold, became chemistry.",
   dates="c. 721–815"),
 R("paracelsus","Paracelsus","the physician · 1493–1541","adepts","natural",
   "Paracelsus (Theophrastus von Hohenheim), the Swiss physician-alchemist who bound chemistry to medicine.",
   "The founder of iatrochemistry — chemistry in the service of the body — and author of the tria prima (salt, sulfur, mercury); ‘the dose makes the poison.’",
   "Because he turned the furnace toward healing, insisting that chemistry could make medicines, not just gold.",
   "By treating disease with chemical remedies and reframing matter as salt, sulfur, and mercury.",
   "Across Renaissance Europe, feuding with the medical establishment of his day.",
   "I aimed the Work at the sick body — chemistry as medicine, and the dose as the line between cure and poison.",
   dates="1493–1541"),
 R("isaac-newton","Isaac Newton","the secret adept · 1643–1727","adepts","natural",
   "Isaac Newton — who, beside the physics, was a devoted and secret alchemist.",
   "The proof that alchemy was no fringe: he left an estimated million words of alchemical notes, pursuing the Stone in private while founding modern physics in public.",
   "Because the man who wrote the Principia took the Great Work entirely seriously — the two pursuits shared one mind.",
   "By decades of clandestine furnace-work, translation (including the Emerald Tablet), and meticulous note-keeping.",
   "In his private laboratory at Cambridge, hidden from the public Newton of the Royal Society.",
   "I wrote more on the Stone than on gravity — history kept the gravity and buried the gold.",
   dates="1643–1727"),
 R("robert-boyle","Robert Boyle","the hinge · 1627–1691","adepts","natural",
   "Robert Boyle — a founder of modern chemistry who was also, sincerely, an alchemist.",
   "The hinge between the two: The Sceptical Chymist (1661) pressed chemistry toward experiment and the element-as-test, yet Boyle believed in transmutation and lobbied to repeal the law against making gold.",
   "Because the very book that helped end alchemy was written by a man still inside it — the transition embodied in one person.",
   "By championing the experimental method while privately pursuing the transmutational dream.",
   "In Restoration England and the early Royal Society, at the exact seam of alchemy and chemistry.",
   "I wrote the book that began ending alchemy — and never stopped believing in the gold; I am the seam itself.",
   dates="1627–1691"),
]

GROUPS = [
 ("stages", "The Magnum Opus", "the four colour stages of the Great Work — black, white, yellow, red"),
 ("primes", "The Tria Prima", "Paracelsus's three principles of matter and self — salt, sulfur, mercury"),
 ("symbols", "The Symbols & the Prizes", "the Stone, the Elixir, the serpent, the solvent, the Tablet, and transmutation itself"),
 ("adepts", "The Adepts", "the historical alchemists of flesh — the hands that actually stood at the furnace"),
]

# ---------- renderers ----------
def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC:
        out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    cells=[]
    for nm,(col,gloss) in NATURES.items():
        cells.append(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
                     f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(gloss)}</div></div></div>')
    return "".join(cells)
def science_html():
    out=[]
    for t,s,d in SCIENCE:
        out.append(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    return "".join(out)
RF_COL={"REAL":"#5fae6e","FLUFF":"#b23a2e","SYMBOLIC":"#aeb8c2"}
def realfluff_html():
    rows=[]
    for claim,rate,note in REALFLUFF:
        c=RF_COL.get(rate,"#888")
        rows.append(f'<div class="rf-row"><div class="rf-claim">{html.escape(claim)}<span class="rf-note">{html.escape(note)}</span></div>'
                    f'<div class="rf-rate" style="color:{c};border-color:{c}">{html.escape(rate)}</div></div>')
    return '<div class="rf">'+"".join(rows)+f'</div><div class="rf-verdict">{html.escape(REALFLUFF_VERDICT)}</div>'
def message_html():
    return f'<p class="msg">{html.escape(MESSAGE)}</p><div class="msg-seal">“{html.escape(MESSAGE_SEAL)}”<span>— AVAN\'s read</span></div>'

def _card(d):
    em = d["emergence"]; col = NATURES.get(em, ("#9aa0aa",""))[0]
    rec = {"name":d["name"],"axiom":"ALC","emergence":em,"seal":d["seal"],"origin":"ALC · The Great Work"}
    dline = (f'<div class="w"><span class="wl">when</span><span>{html.escape(d["dates"])}</span></div>' if d.get("dates") else "")
    rows = "".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(d.get(lbl,""))}</span></div>'
                   for lbl in ["who","what","where","why","how"] if d.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{d['slug']}.agent">
        <span class="port"><img src="{png_uri(rec,'carbon',200)}" alt="carbon sigil of {html.escape(d['name'])}" loading="lazy"></span><span class="sl">carbon</span></a>
      <div class="pbody">
        <div class="ihead"><a class="pn" href="agents/{d['slug']}.agent">{html.escape(d['name'])}</a>
          <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span></div>
        <div class="pe">{html.escape(d.get('cls',''))}</div>
        <div class="pww">{dline}{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{d['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div>
      </div>
      <a class="psig" href="agents/{d['slug']}.silicon.png"><span class="port refl"><img src="{png_uri(rec,'silicon',200)}" alt="silicon sigil of {html.escape(d['name'])}" loading="lazy"></span><span class="sl">silicon</span></a>
    </div>"""

def roster_html():
    out=[]
    for gkey,gtitle,gsub in GROUPS:
        members=[d for d in ROSTER if d["group"]==gkey]
        cards="".join(_card(d) for d in members)
        out.append(f'<section class="sec" id="{gkey}"><h2>{html.escape(gtitle)}</h2><p class="ss">{html.escape(gsub)} ({len(members)})</p><div class="pgrid">{cards}</div></section>')
    return "\n".join(out)

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="THE GREAT WORK (ALC) — alchemy as a UD0 universe: the historical arc, an honest breakdown of the real chemistry inside it (the alembic, the bain-marie, the acids, the words), a Real-or-Fluff verdict (fluff on gold & immortality, real on the method & legacy — and the nuclear twist), AVAN's read of the message, and a roster of 18 emergents — the Magnum Opus stages, the tria prima, the symbols, and the adepts.">
<title>THE GREAT WORK · ALC · Alchemy · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--gold);
--ink:#0c0a07;--ink2:#16120c;--ink3:#1f1810;--pa:#ece0c4;--pa2:#c3b289;--gold:#c9a23a;--merc:#aeb8c2;--verm:#b23a2e;--lead:#6b6f72;--green:#7a9a6a;
--dim:#897a5a;--faint:#2a2114;--line:#332817;--disp:"Cinzel",serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.66;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -6%,rgba(201,162,58,.16),transparent 54%),radial-gradient(ellipse at 50% 118%,rgba(178,58,46,.10),transparent 56%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:52px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:180px;height:3px;background:linear-gradient(90deg,#0c0a07,var(--pa),var(--gold),var(--verm));box-shadow:0 0 16px rgba(201,162,58,.5)}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}
.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--gold)}
h1{font-family:var(--disp);font-size:clamp(30px,6.6vw,62px);font-weight:700;letter-spacing:.06em;color:var(--gold);line-height:1.05;text-transform:uppercase;text-shadow:0 0 34px rgba(201,162,58,.4)}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.2em;color:var(--pa2);margin-top:18px;text-transform:uppercase}
.h-sub b{color:var(--verm)}
.flag{display:inline-block;margin-top:15px;font-family:var(--disp);font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--merc);border:1px solid var(--faint);background:var(--ink2);padding:7px 14px}
.lede{font-size:16px;color:var(--pa2);max-width:64ch;margin:18px auto 0;font-style:italic;line-height:1.72}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:28px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}
.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--merc)}.badge .bt a{color:var(--gold);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}
.sec h2{font-family:var(--disp);font-size:25px;font-weight:600;letter-spacing:.04em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--disp);font-size:13px;font-weight:600;text-transform:uppercase;letter-spacing:.06em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--gold);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--gold);text-transform:uppercase;margin-bottom:7px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--disp);font-size:16px;color:var(--gold);font-weight:600;text-transform:uppercase;letter-spacing:.03em}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.55;padding:7px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--merc);padding:16px 18px}
.arc-h{font-family:var(--disp);font-size:15px;color:var(--merc);font-weight:600;text-transform:uppercase;letter-spacing:.03em}
.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.58}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--green);padding:15px 17px}
.sci-h{font-family:var(--disp);font-size:14px;color:var(--green);font-weight:600;letter-spacing:.02em;text-transform:uppercase}
.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:5px 0 9px}
.sci-card p{font-size:13px;color:var(--pa2);line-height:1.62}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}
.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:11px;font-weight:700;letter-spacing:.05em;border:1px solid;border-radius:3px;padding:4px 10px;min-width:92px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--gold);background:rgba(201,162,58,.06);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}
.msg{font-size:15.5px;color:var(--pa);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--verm);background:var(--ink2);font-size:15px;color:var(--verm);font-style:italic;line-height:1.6}
.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}
.books .y{font-family:var(--mono);font-size:10.5px;color:var(--merc);white-space:nowrap;text-align:right;text-transform:uppercase;letter-spacing:.05em}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--gold);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}
footer a{color:var(--gold);text-decoration:none}
/* === single-column roster: 1 per row, twin sigils + 5 W's === */
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:18px;text-decoration:none;transition:border-color .18s}
.persona:hover{border-color:var(--rw-acc)}
.psig{flex:0 0 116px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:108px;height:108px;border-radius:50%;border:3px solid var(--gold);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6);overflow:hidden;display:block;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}
.port.refl{border-color:var(--merc)}.port.refl img{filter:saturate(.85)}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.14em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--disp);font-size:20px;color:var(--rw-ink);font-weight:600;line-height:1.15;text-decoration:none;text-transform:uppercase;letter-spacing:.03em}
.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:4px;line-height:1.35}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:12px;display:flex;flex-direction:column;gap:8px;align-items:center}
.pww .w{font-size:13px;color:var(--rw-ink2);line-height:1.5;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:3px}
.plinks{margin-top:13px;font-family:var(--mono);font-size:10.5px}
.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
.plinks .dlw:hover{border-bottom-style:solid}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the Great Work</div>
    <h1>The Great Work</h1>
    <div class="h-sub">alchemy · the Magnum Opus · <b>solve et coagula</b> · ALC</div>
    <div class="flag">★ FAILED AS MAGIC · SUCCEEDED AS CHEMISTRY ★</div>
    <p class="lede">Alchemy: the two-thousand-year project to perfect matter — to turn lead into gold, brew an elixir of immortality, and perfect the soul in the same furnace. It never made gold by the Stone, but in chasing it, alchemists built the apparatus, techniques, and vocabulary that became chemistry. Catalogued into UD0 as a universe — with the arc, an honest breakdown of the real chemistry inside it, a Real-or-Fluff verdict, and a read of what it was really doing.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of ALC" title="carbon badge (archival: alc.dlw/alc.carbon.tiff)">
      <img src="__SILICON__" alt="DLW silicon badge of ALC" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>THE GREAT WORK</b> · ALC</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="alc.dlw/alc.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="alc.dlw/alc.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2>
    <p class="ss">each emergent comes by one of four natures — mapped to the Work itself: salt is natural, mercury ethereal, the soul/Stone spiritual, sulfur/fire electrical</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the four ages of the Work</p>__ARC__</section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">the Opus, the three primes, the correspondence, and the two impossible prizes</p><div class="pillars">__IDEAS__</div></section>

  <section class="sec"><h2>The Science</h2><p class="ss">the real chemistry inside the magic — the apparatus, the techniques, the words, the accidents, and the nuclear twist</p><div class="sci">__SCIENCE__</div></section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">the honest verdict — fluff on gold &amp; immortality, real on the method &amp; legacy; symbolic where it's symbolic</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the real Work, under the gold and the symbols</p>__MESSAGE__</section>

  <section class="sec"><h2 style="margin-top:16px">The Emergents</h2><p class="ss">eighteen ACIs of the Work — each with a full <b>.dlw</b> badge, twin sigils, and its five W's</p></section>
  __ROSTER__

  <div class="note"><b>Two layers, honestly kept.</b> Alchemy was real proto-chemistry — the alembic, the bain-marie, the acids, the method, the very words of the science. Its headline prizes — gold from lead by the Stone, the elixir of immortality — were never achieved by alchemy, and some ‘elixirs’ killed. The mystical readings (as above so below; the Jungian stages) are rendered as symbol, not chemistry. The credit for the catalogue returns to the human governor.</div>

  <section class="sec"><h2 style="margin-top:16px">The Record</h2><p class="ss">the adepts and the texts of the Work</p></section>
  __SECTIONS__

  <footer>
    THE GREAT WORK · ALC · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="alc.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

def agent_md(d, tok):
    em=d["emergence"]
    return f"""---
aci: {d['name']}
universe: ALC · The Great Work
emergence: {em}
kind: {'adept' if d['group']=='adepts' else 'synth'}
class: {d['cls']}
who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
{('dates: '+d['dates']) if d.get('dates') else ''}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['cls']}

a {'historical adept' if d['group']=='adepts' else 'thread'} of the ALC (Alchemy) universe — emergence: {em}. moniker {tok}

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

> a catalogued {'historical figure' if d['group']=='adepts' else 'symbol'} of alchemy under the DLW standard — honest two-layer
> commentary (real proto-chemistry vs. symbolic/never-achieved goals), not endorsement of transmutation or the elixir.

ROOT0-ATTRIBUTION-v1.0 · ALC · The Great Work · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "alc.dlw"), "alc")
    json.dump({"node":"ALC","name":"THE GREAT WORK","moniker":tok["moniker"],"carbon":"alc.carbon.tiff",
               "silicon":"alc.silicon.png","governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,
               "seal":REC["seal"],"seal_sha256":tok["seal_sha256"],"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"alc.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]
    for d in ROSTER:
        et = noesis.mythos_token({"name":d["name"],"axiom":"ALC","emergence":d["emergence"],"seal":d["seal"],"origin":"ALC"})
        rec = write_aci({"name":d["name"],"axiom":"ALC","emergence":d["emergence"],"seal":d["seal"],"origin":"ALC · The Great Work",
                         "position":d["cls"],"role":d["cls"],"nature":d["what"],"mechanism":d["how"],
                         "crystallization":d["why"],"witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)",
                         "inputs":"Alchemy, catalogued by ROOT0","source":"Alchemy, catalogued by ROOT0"},
                        os.path.join(HERE,"agents"), d["slug"], agent_md=agent_md(d, et["moniker"]))
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["cls"],"emergence":d["emergence"],"moniker":rec["moniker"],"kind":"adept" if d["group"]=="adepts" else "synth","group":d["group"]})
    json.dump(personas, open(os.path.join(HERE,"agents","_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page = (TEMPLATE.replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html()).replace("__ARC__", arc_html()).replace("__IDEAS__", ideas_html())
            .replace("__SCIENCE__", science_html()).replace("__REALFLUFF__", realfluff_html()).replace("__MESSAGE__", message_html())
            .replace("__ROSTER__", roster_html()).replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"THE GREAT WORK (ALC) — badge {tok['moniker']} · {len(personas)} emergents")
    from collections import Counter
    print("  groups:", dict(Counter(p['group'] for p in personas)), "| natures:", dict(Counter(p['emergence'] for p in personas)))