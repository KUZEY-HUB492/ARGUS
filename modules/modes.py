from modules.apps import uygulama_ac
from modules.web import site_ac


def mod_calistir(mod):

    mod = mod.lower()

    if mod == "oyun":
        uygulama_ac("riot")
        return "🎮 Oyun modu etkinleştirildi."

    elif mod == "geliştirme":
        uygulama_ac("vs code")
        return "💻 Geliştirme modu etkinleştirildi."

    elif mod == "yayın":
        uygulama_ac("obs")
        site_ac("kick")
        return "📺 Yayın modu etkinleştirildi."

    return None