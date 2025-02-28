import sys
import os
import shutil
import json
import webbrowser
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QLineEdit, QDialog, QTextEdit, QComboBox,
    QListWidget, QCheckBox, QScrollArea, QFrame, QMessageBox, QTabWidget, QColorDialog
)
from PyQt6.QtGui import QFont, QIcon, QColor
from PyQt6.QtCore import Qt

CONFIG_DIR = os.path.expanduser("~/.cssolauncher")
CONFIG_FILE = os.path.join(CONFIG_DIR, "launcher_config.json")

# FPS Boost config for CSSO
CSSO_FPSBOOST_CONFIG = """
//Graphical Settings\\


//Graphical Settings\\
r_decal_cullsize	 "0"
r_decals "0"
mp_decals "0"
mat_antialias "0"
mat_forceaniso "0"
mat_trilinear "0"
mat_clipz "0"
mat_disable_bloom "0"
mat_wateroverlaysize "0"
mat_debug_postprocessing_effects "0"
mat_debugdepthmode "0"
mat_debugdepthval "128"
mat_debugdepthvalmax "256"
mat_compressedtextures "1"
mat_filterlightmaps "1"
mat_forcehardwaresync "0"
mat_parallaxmap "0"
mat_hdr_level "0"
mat_bloomscale "0"
mat_forcemanagedtextureintohardware "0"
mat_fastnobump "1"
mat_debug_postprocessing_effects "0"
mat_debugdepthmode "0"
mat_debugdepthval "128"
mat_debugdepthvalmax "256"
mat_compressedtextures "1"
mat_filterlightmaps "1"
mat_forcehardwaresync "0"
mat_reducefillrate "1"
mat_disable_bloom "1"
mat_hdr_enabled "0"
mat_parallaxmap "0"
mat_hdr_level "0"
mat_bloomscale "0"
mat_forcemanagedtextureintohardware "0"
mat_fastnobump "1"
mat_specular "0"
mat_bumpmap "0"
mat_bufferprimitives "1"
mat_disable_lightwarp "1"
mat_framebuffercopyoverlaysize "0"
mat_disable_ps_patch "1"
mat_envmapsize "0"
mat_envmaptgasize "0"
mat_disable_fancy_blending "1"
mat_autoexposure_max "0"
mat_autoexposure_min "0"
mat_alphacoverage "0"
mat_bloom_scalefactor_scalar "0"
mat_maxframelatency "0"
mat_max_worldmesh_vertices "0"
mat_software_aa_blur_one_pixel_lines "0"
mat_software_aa_strength "0"
mat_software_aa_strength_vgui "0"
mat_software_aa_tap_offset "0"
mat_picmip "2"
mat_clipz "1"
mat_vsync "0"
mat_monitorgamma "1.6"
mat_shadowstate "0"
r_3dnow "1"
r_ropetranslucent "0"
r_drawdetailprops "0"
r_drawflecks "0"
r_shadows "0"
r_shadowmaxrendered "32"
r_dynamic "0"
r_3dsky "0"
r_propsmaxdist "0"
r_worldlights "1"
r_renderoverlayfragment "0"
r_eyes "0"
r_teeth "0"
r_maxdlights "32"
r_maxnewsamples "0"
r_maxsampledist "0"
r_norefresh "0"
r_minnewsamples "0"
r_maxdlights "32"
r_maxnewsamples "0"
r_maxsampledist "0"
r_norefresh "0"
r_minnewsamples "0"
r_forcewaterleaf "1"
r_shadows "0"
r_eyes "0"
r_eyeglintlodpixels "0"
r_eyesize "0"
r_eyeshift_z "0"
r_shadowrendertotexture "1"
r_flex "0"
r_eyeshift_y "0"
r_eyeshift_x "0"
r_eyemove "0"
r_eyegloss "0"
r_teeth "0"
r_worldlightmin "0"
r_waterforcereflectentities "0"
r_worldlights "0"
r_PhysPropStaticLighting "0"
r_cheapwaterend "1"
r_cheapwaterstart "1"
r_updaterefracttexture "0"
r_WaterDrawReflection "0"
r_WaterDrawRefraction "1"
r_drawflecks "0"
r_dopixelvisibility "0"
r_renderoverlayfragment "0"
r_occlusion "0"
r_shadowmaxrendered "-1"
r_rootlod "2"
r_lod "2"
r_drawbatchdecals "0"
r_spray_lifetime "1"
r_ambientboost "0"
r_ambientfactor "1"
r_waterforceexpensive "0"
r_ropetranslucent "0"
r_dynamic "0"
r_lightaverage "1"
r_3dsky "0"
r_sse2 "1"
r_maxmodeldecal "0"
r_drawmodeldecals "0"
r_bloomtintg "0"
r_bloomtintb "0"
r_bloomtintexponent "0"
r_bloomtintr "0"
r_drawdetailprops "0"
r_flashlightrendermodels "0"
r_hunkalloclightmaps "0"
r_lightcache_zbuffercache "0"
r_propsmaxdist "0"
r_staticprop_lod "3"
r_sse_s "1"
r_queued_ropes "1"
rope_smooth "0"
rope_wind_dist "0"
rope_collide "0"
rope_subdiv "0"
rope_smooth_maxalphawidth "0"
rope_smooth_maxalpha "0"
rope_smooth_enlarge "0"
rope_wind_dist "0.01"
rope_subdiv "0"
rope_smooth_minwidth "0"
rope_smooth_minalpha "0"
rope_averagelight "0"
rope_smooth "0"
rope_shake "0"
rope_collide "0"
violence_ablood "1"
violence_agibs "1"
violence_hblood "1"
violence_hgibs "1"
cl_new_impact_effects "1"
cl_radaralpha "255"
cl_ragdoll_physics_enable "1"
cl_ragdoll_collide "0"
cl_sway_interp "0"
cl_phys_props_max "0"
cl_drawmonitors "0"
cl_ejectbrass "0"
cl_forcepreload "1"
cl_show_splashes "0"
cl_detail_avoid_force "0"
cl_detail_avoid_radius "0"
cl_detail_avoid_recover_speed "0"
cl_detail_max_sway "0"
cl_forcepreload "1"
cl_drawmonitors "0"
cl_show_splashes "0"
cl_detail_avoid_force "0"
cl_detail_avoid_radius "0"
cl_detail_avoid_recover_speed "0"
cl_wpn_sway_interp "0.1"
cl_detail_max_sway "0"
cl_rumblescale "0"
cl_disablefreezecam "0"
cl_clearhinthistory "1"
cl_detaildist "0"
cl_detailfade "0"
cl_debugrumble "0"
cl_playerspraydisable "1"
cl_showhelp "0"
cl_phys_props_max "0"
cl_phys_props_enable "0"
budget_peaks_window "0"
budget_show_peaks "0"
budget_averages_window "0"
budget_background_alpha "0"
budget_show_averages "0"
budget_show_history "0"
budget_history_range_ms "5"
budget_history_numsamplesvisible "0"
texture_budget_background_alpha "9999999"
texture_budget_panel_height "0"
texture_budget_panel_width "0"
g_ragdoll_fadespeed "0"
g_ragdoll_lvfadespeed "0"
gl_clear "1"
lod_TransitionDist "0"
flex_smooth "0"
showhitlocation "1"
dsp_water "14"
blink_duration "0"
weapon_showproficiency "1"
prop_active_gib_limit "0"
adsp_debug "0"
cl_show_splashes "0"
con_filter_text "Too many vertex" 
con_filter_text_out "Too many vertex" 
con_filter_enable "2"



//Multi-Core Rendering Settings\\
mat_queue_mode "2"
cl_interp_threadmodeticks "0" 
cl_threaded_bone_setup "0"
cl_threaded_client_leaf_system "0"
host_thread_mode "0"
r_threaded_client_shadow_manager "0"
r_threaded_particles "1"
r_threaded_renderables "0"
r_queued_decals "0"
r_queued_post_processing "0"
r_queued_ropes "0"
threadpool_affinity "0"
mp_usehwmmodels "-1"
mp_usehwmvcds "-1"

// No motion blur

mat_motion_blur_enabled "0"
mat_motion_blur_falling_intensity "0"
mat_motion_blur_forward_enabled "0"
mat_motion_blur_strength "0"

// Shadows 100FPS

r_shadows "1"                      // Habilita las sombras
r_shadowrendertotexture "0"        // Desactiva sombras de alta calidad
r_shadowmaxrendered "10"           // Reduce la cantidad máxima de sombras renderizadas
r_shadowradius "0"                 // Reduce el radio de las sombras
r_flashlightrendermodels "0"       // Desactiva sombras dinámicas de la linterna
mat_shadowstate "0"                // Desactiva efectos avanzados de sombras

//Netcode Settings\\
rate "128000"
cl_cmdrate "128"
cl_updaterate "128"
cl_interp "0"
cl_interp_ratio "1"
cl_lagcompensation "1"
cl_predictweapons "1"
cl_smooth "0"
cl_smoothtime "0"
cl_pred_optimize "2"
cl_idealpitchscale "0.02"
net_scale "5"
net_showevents "0"
net_chokeloop "0"
cl_allowupload "1"	
cl_allowdownload "1"
cl_downloadfilter "nosounds"

//Sound Settings\\

snd_digital_surround "1"   
snd_surround_speakers "0"   
volume "1.0" 
snd_musicvolume "0.0" 
dsp_slow_cpu "0"   
snd_noextraupdate "1"   
voice_dsound "0"   
snd_mixahead "0.1" 
soundscape_flush

//Graphical Settings\\
		
//Multi-Core Rendering Settings\\
mat_queue_mode "2"
cl_interp_threadmodeticks "0" 
cl_threaded_bone_setup "0"
cl_threaded_client_leaf_system "0"
host_thread_mode "0"
r_threaded_client_shadow_manager "0"
r_threaded_particles "1"
r_threaded_renderables "0"
r_queued_decals "0"
r_queued_post_processing "0"
r_queued_ropes "0"
threadpool_affinity "0"
mp_usehwmmodels "-1"
mp_usehwmvcds "-1"



//Other Settings\\

fps_max_menu "65"

fps_max "0"

cl_minmodels "0"

cl_min_ct ""	

cl_min_t ""
cl_righthand "1"

cl_showpos "0"


cl_showfps "2"

hud_showtargetid "1"

cl_autohelp "0"

hud_fastswitch "1"

cl_autowepswitch "0"

voice_enable "1"

setinfo zb_wantautocashcalling "1"

save_changes

save



//Set-Launch Options Settings\\

-console
-high
-dxlevel 90
-nojoy
-noforcemaccel 
-noforcemparms


clear



echo "| ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"
echo "|               ROXXX High FPS CFG               |"
echo "|                                                |"
echo "|                     ROXXX                      |"
echo "|                                                |"
echo "|                                                |"
echo "| ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"
// Mensaje de confirmación al cargar el archivo
echo "Configuración personalizada cargada correctamente."
"""

# FPS Boost config for CSGO
CSGO_FPSBOOST_CONFIG = """
//Graphical Settings\\

//Graphical Settings
r_decal_cullsize "0"
r_decals "0"
mp_decals "0"
mat_antialias "0"
mat_forceaniso "0"
mat_trilinear "0"
mat_clipz "0"
mat_disable_bloom "0"
mat_compressedtextures "1"
mat_filterlightmaps "1"
mat_forcehardwaresync "0"
mat_hdr_level "0"
mat_bloomscale "0"
mat_forcemanagedtextureintohardware "0"
mat_fastnobump "1"
mat_compressedtextures "1"
mat_filterlightmaps "1"
mat_forcehardwaresync "0"
mat_reducefillrate "1"
mat_disable_bloom "1"
mat_hdr_enabled "0"
mat_hdr_level "0"
mat_bloomscale "0"
mat_forcemanagedtextureintohardware "0"
mat_fastnobump "1"
mat_specular "0"
mat_bumpmap "0"
mat_bufferprimitives "1"
mat_disable_lightwarp "1"
mat_framebuffercopyoverlaysize "0"
mat_autoexposure_max "0"
mat_autoexposure_min "0"
mat_alphacoverage "0"
mat_bloom_scalefactor_scalar "0"
mat_maxframelatency "0"
mat_max_worldmesh_vertices "0"
mat_software_aa_blur_one_pixel_lines "0"
mat_software_aa_strength "0"
mat_software_aa_strength_vgui "0"
mat_software_aa_tap_offset "0"
mat_picmip "2"
mat_clipz "1"
mat_vsync "0"
mat_monitorgamma "1.6"
mat_shadowstate "0"
r_3dnow "1"
r_ropetranslucent "0"
r_drawdetailprops "0"
r_drawflecks "0"
r_shadows "0"
r_shadowmaxrendered "32"
r_dynamic "0"
r_3dsky "0"
r_propsmaxdist "0"
r_worldlights "1"
r_renderoverlayfragment "0"
r_eyes "0"
r_teeth "0"
r_maxdlights "32"
r_maxnewsamples "0"
r_maxsampledist "0"
r_norefresh "0"
r_minnewsamples "0"
r_maxdlights "32"
r_maxnewsamples "0"
r_maxsampledist "0"
r_norefresh "0"
r_minnewsamples "0"
r_forcewaterleaf "1"
r_shadows "0"
r_eyes "0"
r_eyeglintlodpixels "0"
r_eyesize "0"
r_eyeshift_z "0"
r_shadowrendertotexture "1"
r_flex "0"
r_eyeshift_y "0"
r_eyeshift_x "0"
r_eyemove "0"
r_eyegloss "0"
r_teeth "0"
r_worldlightmin "0"
r_waterforcereflectentities "0"
r_worldlights "0"
r_PhysPropStaticLighting "0"
r_cheapwaterend "1"
r_cheapwaterstart "1"
r_updaterefracttexture "0"
r_WaterDrawReflection "0"
r_WaterDrawRefraction "1"
r_drawflecks "0"
r_dopixelvisibility "0"
r_renderoverlayfragment "0"
r_occlusion "0"
r_shadowmaxrendered "-1"
r_rootlod "2"
r_lod "2"
r_drawbatchdecals "0"
r_spray_lifetime "1"
r_ambientboost "0"
r_ambientfactor "1"
r_waterforceexpensive "0"
r_ropetranslucent "0"
r_dynamic "0"
r_lightaverage "1"
r_3dsky "0"
r_sse2 "1"
r_maxmodeldecal "0"
r_drawmodeldecals "0"
r_bloomtintg "0"
r_bloomtintb "0"
r_bloomtintexponent "0"
r_bloomtintr "0"
r_drawdetailprops "0"
r_flashlightrendermodels "0"
r_hunkalloclightmaps "0"
r_lightcache_zbuffercache "0"
r_propsmaxdist "0"
r_staticprop_lod "3"
r_sse_s "1"
r_queued_ropes "1"
rope_smooth "0"
rope_wind_dist "0"
rope_collide "0"
rope_subdiv "0"
rope_smooth_maxalphawidth "0"
rope_smooth_maxalpha "0"
rope_smooth_enlarge "0"
rope_wind_dist "0.01"
rope_subdiv "0"
rope_smooth_minwidth "0"
rope_smooth_minalpha "0"
rope_averagelight "0"
rope_smooth "0"
rope_shake "0"
rope_collide "0"
violence_ablood "1"
violence_agibs "1"
violence_hblood "1"
violence_hgibs "1"
cl_new_impact_effects "1"
cl_radaralpha "255"
cl_ragdoll_physics_enable "1"
cl_ragdoll_collide "0"
cl_sway_interp "0"
cl_phys_props_max "0"
cl_drawmonitors "0"
cl_ejectbrass "0"
cl_forcepreload "1"
cl_show_splashes "0"
cl_detail_avoid_force "0"
cl_detail_avoid_radius "0"
cl_detail_avoid_recover_speed "0"
cl_detail_max_sway "0"
cl_forcepreload "1"
cl_drawmonitors "0"
cl_show_splashes "0"
cl_detail_avoid_force "0"
cl_detail_avoid_radius "0"
cl_detail_avoid_recover_speed "0"
cl_wpn_sway_interp "0.1"
cl_detail_max_sway "0"
cl_rumblescale "0"
cl_disablefreezecam "0"
cl_clearhinthistory "1"
cl_detaildist "0"
cl_detailfade "0"
cl_debugrumble "0"
cl_playerspraydisable "1"
cl_showhelp "0"
cl_phys_props_max "0"
cl_phys_props_enable "0"
budget_peaks_window "0"
budget_show_peaks "0"
budget_averages_window "0"
budget_background_alpha "0"
budget_show_averages "0"
budget_show_history "0"
budget_history_range_ms "5"
budget_history_numsamplesvisible "0"
texture_budget_background_alpha "9999999"
texture_budget_panel_height "0"
texture_budget_panel_width "0"
g_ragdoll_fadespeed "0"
g_ragdoll_lvfadespeed "0"
gl_clear "1"
lod_TransitionDist "0"
flex_smooth "0"
showhitlocation "1"
dsp_water "14"
blink_duration "0"
weapon_showproficiency "1"
prop_active_gib_limit "0"
adsp_debug "0"
cl_show_splashes "0"
con_filter_text "Too many vertex"
con_filter_text_out "Too many vertex"
con_filter_enable "2"

//Multi-Core Rendering Settings
mat_queue_mode "2"
cl_interp_threadmodeticks "0"
cl_threaded_bone_setup "0"
cl_threaded_client_leaf_system "0"
host_thread_mode "0"
r_threaded_client_shadow_manager "0"
r_threaded_particles "1"
r_threaded_renderables "0"
r_queued_decals "0"
r_queued_post_processing "0"
r_queued_ropes "0"
threadpool_affinity "0"
mp_usehwmmodels "-1"
mp_usehwmvcds "-1"

// No motion blur

mat_motion_blur_enabled "0"
mat_motion_blur_falling_intensity "0"
mat_motion_blur_forward_enabled "0"
mat_motion_blur_strength "0"

// Shadows 100FPS

r_shadows "1" // Habilita las sombras
r_shadowrendertotexture "0" // Desactiva sombras de alta calidad
r_shadowmaxrendered "10" // Reduce la cantidad máxima de sombras renderizadas
r_shadowradius "0" // Reduce el radio de las sombras
r_flashlightrendermodels "0" // Desactiva sombras dinámicas de la linterna
mat_shadowstate "0" // Desactiva efectos avanzados de sombras

//Netcode Settings
rate "128000"
cl_cmdrate "128"
cl_updaterate "128"
cl_interp "0"
cl_interp_ratio "1"
cl_lagcompensation "1"
cl_predictweapons "1"
cl_smooth "0"
cl_smoothtime "0"
cl_pred_optimize "2"
cl_idealpitchscale "0.02"
net_scale "5"
net_showevents "0"
net_chokeloop "0"
cl_allowupload "1"
cl_allowdownload "1"
cl_downloadfilter "nosounds"

//Sound Settings\

snd_digital_surround "1"
snd_surround_speakers "0"
volume "1.0"
snd_musicvolume "0.0"
dsp_slow_cpu "0"
snd_noextraupdate "1"
voice_dsound "0"
snd_mixahead "0.1"
soundscape_flush

//Graphical Settings\

//Multi-Core Rendering Settings
mat_queue_mode "2"
cl_interp_threadmodeticks "0"
cl_threaded_bone_setup "0"
cl_threaded_client_leaf_system "0"
host_thread_mode "0"
r_threaded_client_shadow_manager "0"
r_threaded_particles "1"
r_threaded_renderables "0"
r_queued_decals "0"
r_queued_post_processing "0"
r_queued_ropes "0"
threadpool_affinity "0"
mp_usehwmmodels "-1"
mp_usehwmvcds "-1"

//Other Settings\

fps_max_menu "65"

fps_max "0"

cl_minmodels "0"

cl_min_ct ""

cl_min_t ""
cl_righthand "1"

cl_showpos "0"

cl_showfps "2"

hud_showtargetid "1"

cl_autohelp "0"

hud_fastswitch "1"

cl_autowepswitch "0"

voice_enable "1"

setinfo zb_wantautocashcalling "1"

save_changes

save

//Set-Launch Options Settings\

-console
-high
-dxlevel 90
-nojoy
-noforcemaccel
-noforcemparms

clear

echo "| ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"
echo "| ROXXX High FPS CFG |"
echo "| |"
echo "| ROXXX |"
echo "| |"
echo "| |"
echo "| ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"
// Mensaje de confirmación al cargar el archivo
echo "Configuración personalizada cargada correctamente."
"""

# Función para verificar y copiar el icono si es necesario
def ensure_icon_exists():
    # Directorio donde se ejecuta la aplicación
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Posibles ubicaciones del icono
    source_paths = [
        os.path.join(base_dir, "assets", "icono.ico"),
        "assets/icono.ico"
    ]
    
    # Directorio de destino para el icono en la configuración
    icon_dest = os.path.join(CONFIG_DIR, "icono.ico")
    
    # Si el icono ya existe en el directorio de configuración, no es necesario copiarlo
    if os.path.exists(icon_dest):
        return icon_dest
    
    # Intentar encontrar el icono en alguna de las ubicaciones posibles
    for source_path in source_paths:
        if os.path.exists(source_path):
            try:
                # Crear directorio de configuración si no existe
                os.makedirs(CONFIG_DIR, exist_ok=True)
                # Copiar el icono al directorio de configuración
                shutil.copy2(source_path, icon_dest)
                print(f"Icono copiado a: {icon_dest}")
                return icon_dest
            except Exception as e:
                print(f"Error al copiar el icono: {e}")
    
    return None

class LauncherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CS Launcher")
        
        # Gestionar icono de la aplicación
        icon_path = ensure_icon_exists()
        if icon_path and os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            # Buscar el icono en diferentes ubicaciones
            icon_paths = [
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "icono.ico"),
                "assets/icono.ico",
                os.path.join(os.path.expanduser("~"), ".cssolauncher", "icono.ico")
            ]
            
            # Intentar cargar el icono desde alguna de las rutas disponibles
            icon_found = False
            for path in icon_paths:
                if os.path.exists(path):
                    self.setWindowIcon(QIcon(path))
                    icon_found = True
                    break
                    
            # Si no se encuentra el icono, mostrar mensaje en la consola (no afecta al usuario)
            if not icon_found:
                print("Advertencia: No se pudo encontrar el icono de la aplicación.")
        
        # Crear directorio de configuración si no existe
        os.makedirs(CONFIG_DIR, exist_ok=True)

        # Idiomas disponibles
        self.languages = {
            "Es": {
                "welcome": "Bienvenido",
                "boost": "Activar Boost",
                "disable_boost": "Desactivar Boost",
                "discord": "Discord",
                "local_files": "Archivos Locales",
                "launch_game": "Abrir Juego",
                "launch_params": "Parámetros de Lanzamiento",
                "game_path_not_set": "Ruta del juego no establecida",
                "game_path": "Ruta del juego",
                "official_page": "Página Oficial",
                "report_errors": "Selector de Skins",
                "settings": "Configuración",
                "save": "Guardar",
                "version": "Versión <span style='color: #E14A00;'>Alpha</span> <span style='color: #EBEFF3;'>1.1</span>",
                "language_label": "Idioma seleccionado: Español",
                "language_text": "Idioma",
                "select_skins": "Selector de Skins",
                "selected_vpks": "VPKs Seleccionados",
                "no_vpks_found": "No se encontraron archivos VPK",
                "skin_select_success": "Selección de skins guardada correctamente",
                "vpk_applied": "VPKs aplicados correctamente",
                "vpk_disabled": "VPKs desactivados correctamente",
                "csso_tab": "CSSO",
                "csgo_tab": "CSGO",
                "settings_title": "Configuración",
                "username": "Nombre de Usuario",
                "background_color": "Color de Fondo",
                "button_color": "Color de Botones",
                "text_color": "Color de Texto",
                "choose_color": "Elegir Color",
                "reset_colors": "Restablecer Colores",
                "cancel": "Cancelar",
                "apply": "Aplicar",
                "local_files_options": "Opciones de Archivos Locales",
                "local_files_management": "Gestión de Archivos Locales",
                "open_main_folder": "Abrir Carpeta Principal de",
                "open_cfg_folder": "Abrir Carpeta de Configuración (cfg)",
                "open_custom_folder": "Abrir Carpeta de Mods (custom)",
                "create_config_backup": "Crear Respaldo de Archivos de Configuración",
                "restore_config_backup": "Restaurar Respaldo de Configuración",
                "select_game_path": "Seleccionar Ruta del Juego",
                "show_disk_info": "Mostrar Información de Espacio en Disco",
                "current_path": "Ruta actual",
                "close": "Cerrar",
                "success": "Éxito",
                "info": "Información",
                "error": "Error",
                "confirm_restore": "¿Estás seguro de restaurar este respaldo? Se sobrescribirán los archivos existentes.",
                "backup_created": "Respaldo creado correctamente en:",
                "backup_restored": "Respaldo restaurado correctamente.",
                "no_backups": "No hay respaldos disponibles para restaurar.",
                "path_updated": "Ruta actualizada correctamente.",
                "no_files_to_backup": "No hay archivos de configuración para respaldar.",
                "disk_info": "Información del disco para la unidad que contiene:",
                "total_space": "Espacio total:",
                "used_space": "Espacio usado:",
                "free_space": "Espacio libre:",
                "disk_warning": "⚠️ ADVERTENCIA: Queda muy poco espacio libre en el disco.",
                "disk_info_error": "No se pudo obtener información del disco:",
                "folder_error": "No se pudo abrir la carpeta:"
            },
            "En": {
                "welcome": "Welcome",
                "boost": "Enable Boost",
                "disable_boost": "Disable Boost",
                "discord": "Discord",
                "local_files": "Local Files",
                "launch_game": "Launch Game",
                "launch_params": "Launch Parameters",
                "game_path_not_set": "Game path not set",
                "game_path": "Game Path",
                "official_page": "Official Page",
                "report_errors": "Skin Selector",
                "settings": "Settings",
                "save": "Save",
                "version": "Version <span style='color: #E14A00;'>Alpha</span> <span style='color: #EBEFF3;'>1.1</span>",
                "language_label": "Selected Language: English",
                "language_text": "Language",
                "select_skins": "Skin Selector",
                "selected_vpks": "Selected VPKs",
                "no_vpks_found": "No VPK files found",
                "skin_select_success": "Skin selection saved successfully",
                "vpk_applied": "VPKs applied successfully",
                "vpk_disabled": "VPKs disabled successfully",
                "csso_tab": "CSSO",
                "csgo_tab": "CSGO",
                "settings_title": "Settings",
                "username": "Username",
                "background_color": "Background Color",
                "button_color": "Button Color",
                "text_color": "Text Color",
                "choose_color": "Choose Color",
                "reset_colors": "Reset Colors",
                "cancel": "Cancel",
                "apply": "Apply",
                "local_files_options": "Local Files Options",
                "local_files_management": "Local Files Management",
                "open_main_folder": "Open Main Folder of",
                "open_cfg_folder": "Open Configuration Folder (cfg)",
                "open_custom_folder": "Open Mods Folder (custom)",
                "create_config_backup": "Create Configuration Backup",
                "restore_config_backup": "Restore Configuration Backup",
                "select_game_path": "Select Game Path",
                "show_disk_info": "Show Disk Space Information",
                "current_path": "Current path",
                "close": "Close",
                "success": "Success",
                "info": "Information",
                "error": "Error",
                "confirm_restore": "Are you sure you want to restore this backup? Existing files will be overwritten.",
                "backup_created": "Backup created successfully at:",
                "backup_restored": "Backup restored successfully.",
                "no_backups": "No backups available to restore.",
                "path_updated": "Path updated successfully.",
                "no_files_to_backup": "No configuration files to backup.",
                "disk_info": "Disk information for the drive containing:",
                "total_space": "Total space:",
                "used_space": "Used space:",
                "free_space": "Free space:",
                "disk_warning": "⚠️ WARNING: Very little free space left on disk.",
                "disk_info_error": "Could not get disk information:",
                "folder_error": "Could not open folder:"
            },
            "Pt": {
                "welcome": "Bem-vindo",
                "boost": "Ativar Boost",
                "disable_boost": "Desativar Boost",
                "discord": "Discord",
                "local_files": "Arquivos Locais",
                "launch_game": "Abrir Jogo",
                "launch_params": "Parâmetros de Lançamento",
                "game_path_not_set": "Caminho do jogo não definido",
                "game_path": "Caminho do jogo",
                "official_page": "Página Oficial",
                "report_errors": "Seletor de Skins",
                "settings": "Configurações",
                "save": "Salvar",
                "version": "Versão <span style='color: #E14A00;'>Alpha</span> <span style='color: #EBEFF3;'>1.1</span>",
                "language_label": "Idioma selecionado: Português",
                "language_text": "Idioma",
                "select_skins": "Seletor de Skins",
                "selected_vpks": "VPKs Selecionados",
                "no_vpks_found": "Nenhum arquivo VPK encontrado",
                "skin_select_success": "Seleção de skins salva com sucesso",
                "vpk_applied": "VPKs aplicados com sucesso",
                "vpk_disabled": "VPKs desativados com sucesso",
                "csso_tab": "CSSO",
                "csgo_tab": "CSGO",
                "settings_title": "Configurações",
                "username": "Nome de Usuário",
                "background_color": "Cor de Fundo",
                "button_color": "Cor dos Botões",
                "text_color": "Cor do Texto",
                "choose_color": "Escolher Cor",
                "reset_colors": "Restaurar Cores",
                "cancel": "Cancelar",
                "apply": "Aplicar",
                "local_files_options": "Opções de Arquivos Locais",
                "local_files_management": "Gerenciamento de Arquivos Locais",
                "open_main_folder": "Abrir Pasta Principal de",
                "open_cfg_folder": "Abrir Pasta de Configuração (cfg)",
                "open_custom_folder": "Abrir Pasta de Mods (custom)",
                "create_config_backup": "Criar Backup de Arquivos de Configuração",
                "restore_config_backup": "Restaurar Backup de Configuração",
                "select_game_path": "Selecionar Caminho do Jogo",
                "show_disk_info": "Mostrar Informações de Espaço em Disco",
                "current_path": "Caminho atual",
                "close": "Fechar",
                "success": "Sucesso",
                "info": "Informação",
                "error": "Erro",
                "confirm_restore": "Tem certeza que deseja restaurar este backup? Arquivos existentes serão sobrescritos.",
                "backup_created": "Backup criado com sucesso em:",
                "backup_restored": "Backup restaurado com sucesso.",
                "no_backups": "Não há backups disponíveis para restaurar.",
                "path_updated": "Caminho atualizado com sucesso.",
                "no_files_to_backup": "Não há arquivos de configuração para fazer backup.",
                "disk_info": "Informações do disco para a unidade que contém:",
                "total_space": "Espaço total:",
                "used_space": "Espaço usado:",
                "free_space": "Espaço livre:",
                "disk_warning": "⚠️ AVISO: Muito pouco espaço livre no disco.",
                "disk_info_error": "Não foi possível obter informações do disco:",
                "folder_error": "Não foi possível abrir a pasta:"
            },
        }

        # Estado inicial
        self.current_language = "Es"
        self.user_name = "User"
        
        # Configuración de colores por defecto
        self.background_color = "#0A0C0C"
        self.button_color = "#E14A00"
        self.text_color = "#EBEFF3"
        
        # Configuración para CSSO
        self.csso_game_path = None
        self.csso_launch_params = "-game csso -insecure"
        self.csso_boost_enabled = False
        self.csso_custom_launch_params = "-console -high -dxlevel 90 -nojoy -noforcemaccel -noforcemparms"
        self.selected_vpks = []  # Almacena los VPKs seleccionados
        
        # Configuración para CSGO
        self.csgo_game_path = None
        self.csgo_launch_params = "-steam -silent"
        self.csgo_boost_enabled = False
        self.csgo_custom_launch_params = "-console -high -nojoy -noforcemaccel -noforcemparms -d3d9ex"

        # Cargar configuración previa
        self.load_config()
        
        # Aplicar estilo según la configuración cargada
        self.apply_style()

        # Crear pestañas para CSSO y CSGO
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet(f"""
            QTabWidget::pane {{ 
                border: 1px solid #444; 
                background-color: {self.background_color};
            }}
            QTabBar::tab {{ 
                background-color: #222; 
                color: {self.text_color}; 
                padding: 8px 12px; 
                margin-right: 2px; 
            }}
            QTabBar::tab:selected {{ 
                background-color: {self.button_color}; 
                color: #0A0C0C; 
                font-weight: bold;
            }}
        """)
        
        # Crear widgets para las pestañas
        self.csso_tab = QWidget()
        self.csgo_tab = QWidget()
        
        # Configurar pestaña CSSO
        self.setup_csso_tab()
        
        # Configurar pestaña CSGO
        self.setup_csgo_tab()
        
        # Añadir pestañas al control de pestañas
        self.tabs.addTab(self.csso_tab, "CSSO")
        self.tabs.addTab(self.csgo_tab, "CSGO")
        
        # Añadir conexión para detectar cambios de pestaña
        self.tabs.currentChanged.connect(self.on_tab_changed)
        
        # Diseño principal
        main_layout = QVBoxLayout()

        # Etiqueta de bienvenida
        self.welcome_label = QLabel()
        self.welcome_label.setStyleSheet(f"color: {self.text_color};")
        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.welcome_label.setFont(QFont("Montserrat", 16, QFont.Weight.Normal))
        main_layout.addWidget(self.welcome_label)
        
        # Añadir pestañas al diseño principal
        main_layout.addWidget(self.tabs)

        # Botones inferiores adicionales
        self.extra_buttons_layout = QHBoxLayout()

        self.official_label = QLabel()
        self.official_label.setStyleSheet(f"background-color: {self.background_color}; color: {self.button_color}; font-weight: bold;")
        self.official_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.official_label.mousePressEvent = lambda event: self.open_link("https://discord.gg/GwWjBs67Tn")

        # Crear el botón de selector de skins (solo visible en CSSO)
        self.skin_selector_label = QLabel()
        self.skin_selector_label.setStyleSheet(f"background-color: {self.background_color}; color: {self.button_color}; font-weight: bold;")
        self.skin_selector_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.skin_selector_label.mousePressEvent = lambda event: self.open_skin_selector()
        # Inicialmente se configura según la pestaña actual
        self.skin_selector_label.setVisible(self.tabs.currentIndex() == 0)  # Solo visible en CSSO (índice 0)

        self.settings_label = QLabel()
        self.settings_label.setStyleSheet(f"background-color: {self.background_color}; color: {self.button_color}; font-weight: bold;")
        self.settings_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.settings_label.mousePressEvent = lambda event: self.open_settings()

        self.extra_buttons_layout.addWidget(self.official_label)
        self.extra_buttons_layout.addWidget(self.skin_selector_label)
        self.extra_buttons_layout.addWidget(self.settings_label)
        main_layout.addLayout(self.extra_buttons_layout)

        # Diseño inferior
        bottom_layout = QHBoxLayout()

        # Etiqueta de versión (esquina inferior izquierda)
        self.version_label = QLabel()
        self.version_label.setStyleSheet(f"color: {self.text_color};")
        self.version_label.setFont(QFont("Montserrat", 10, QFont.Weight.Normal))
        bottom_layout.addWidget(self.version_label, alignment=Qt.AlignmentFlag.AlignLeft)

        bottom_layout.addStretch()

        # Añadir texto "MADEBY@ROX"
        self.madeby_label = QLabel("MADEBY@ROX")
        self.madeby_label.setStyleSheet(f"color: {self.text_color}; font-size: 8px; font-weight: bold;")
        self.madeby_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Centrar el texto

        # Agregar al layout de la barra inferior
        bottom_layout.addWidget(self.madeby_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Etiqueta "Idioma" y selector de idioma (esquina inferior derecha)
        language_layout = QHBoxLayout()

        self.language_label = QLabel()
        self.language_label.setStyleSheet(f"color: {self.text_color};")
        self.language_label.setFont(QFont("Montserrat", 10, QFont.Weight.Normal))
        language_layout.addWidget(self.language_label)

        self.language_selector = QComboBox()
        self.language_selector.addItems(list(self.languages.keys()))
        self.language_selector.setStyleSheet(f"color: {self.button_color};")
        self.language_selector.setFont(QFont("Montserrat", 10, QFont.Weight.Normal))
        self.language_selector.currentTextChanged.connect(self.change_language)
        language_layout.addWidget(self.language_selector)

        bottom_layout.addStretch()
        bottom_layout.addLayout(language_layout)
        main_layout.addLayout(bottom_layout)

        # Establecer widget central
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Actualizar el texto según el idioma inicial
        self.update_texts()

        # Aplicar skins seleccionadas si hay alguna
        self.apply_selected_vpks()
        
        # Establecer la pestaña actual (esto activará on_tab_changed)
        self.tabs.setCurrentIndex(0)  # CSSO es la pestaña predeterminada

    def on_tab_changed(self, index):
        # Mostrar u ocultar el selector de skins según la pestaña activa
        self.skin_selector_label.setVisible(index == 0)  # Solo visible en CSSO (índice 0)
        self.update_texts()

    def setup_csso_tab(self):
        # Diseño principal de la pestaña CSSO
        csso_layout = QVBoxLayout()
        
        # Botones
        self.csso_boost_button = QPushButton()
        self.csso_boost_button.setStyleSheet(self.button_style())
        self.csso_boost_button.setFont(QFont("Montserrat", 12, QFont.Weight.ExtraBold))
        self.csso_boost_button.setMinimumHeight(50)
        self.csso_boost_button.clicked.connect(lambda: self.toggle_boost("csso"))

        self.csso_discord_button = QPushButton()
        self.csso_discord_button.setStyleSheet(self.button_style())
        self.csso_discord_button.setFont(QFont("Montserrat", 12, QFont.Weight.ExtraBold))
        self.csso_discord_button.setMinimumHeight(50)
        self.csso_discord_button.clicked.connect(lambda: self.open_link("https://discord.gg/N8qAufHRth"))

        self.csso_local_files_button = QPushButton()
        self.csso_local_files_button.setStyleSheet(self.button_style())
        self.csso_local_files_button.setFont(QFont("Montserrat", 12, QFont.Weight.ExtraBold))
        self.csso_local_files_button.setMinimumHeight(50)
        self.csso_local_files_button.clicked.connect(lambda: self.manage_game_path("csso"))

        self.csso_launch_button = QPushButton()
        self.csso_launch_button.setStyleSheet(self.button_style())
        self.csso_launch_button.setFont(QFont("Montserrat", 12, QFont.Weight.ExtraBold))
        self.csso_launch_button.setMinimumHeight(50)
        self.csso_launch_button.clicked.connect(lambda: self.launch_game("csso"))

        self.csso_params_button = QPushButton()
        self.csso_params_button.setStyleSheet(self.button_style())
        self.csso_params_button.setFont(QFont("Montserrat", 12, QFont.Weight.ExtraBold))
        self.csso_params_button.setMinimumHeight(50)
        self.csso_params_button.clicked.connect(lambda: self.set_launch_params("csso"))

        button_layout1 = QHBoxLayout()
        button_layout1.addWidget(self.csso_boost_button)
        button_layout1.addWidget(self.csso_launch_button)

        button_layout2 = QHBoxLayout()
        button_layout2.addWidget(self.csso_discord_button)
        button_layout2.addWidget(self.csso_local_files_button)

        csso_layout.addLayout(button_layout1)
        csso_layout.addLayout(button_layout2)
        csso_layout.addWidget(self.csso_params_button)

        # Ruta del juego
        self.csso_path_label = QLabel()
        self.csso_path_label.setStyleSheet(f"color: {self.text_color};")
        self.csso_path_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        csso_layout.addWidget(self.csso_path_label)
        
        self.csso_tab.setLayout(csso_layout)

    def setup_csgo_tab(self):
        # Diseño principal de la pestaña CSGO
        csgo_layout = QVBoxLayout()
        
        # Botones
        self.csgo_boost_button = QPushButton()
        self.csgo_boost_button.setStyleSheet(self.button_style())
        self.csgo_boost_button.setFont(QFont("Montserrat", 12, QFont.Weight.ExtraBold))
        self.csgo_boost_button.setMinimumHeight(50)
        self.csgo_boost_button.clicked.connect(lambda: self.toggle_boost("csgo"))

        self.csgo_discord_button = QPushButton()
        self.csgo_discord_button.setStyleSheet(self.button_style())
        self.csgo_discord_button.setFont(QFont("Montserrat", 12, QFont.Weight.ExtraBold))
        self.csgo_discord_button.setMinimumHeight(50)
        self.csgo_discord_button.clicked.connect(lambda: self.open_link("https://discord.gg/N8qAufHRth"))

        self.csgo_local_files_button = QPushButton()
        self.csgo_local_files_button.setStyleSheet(self.button_style())
        self.csgo_local_files_button.setFont(QFont("Montserrat", 12, QFont.Weight.ExtraBold))
        self.csgo_local_files_button.setMinimumHeight(50)
        self.csgo_local_files_button.clicked.connect(lambda: self.manage_game_path("csgo"))

        self.csgo_launch_button = QPushButton()
        self.csgo_launch_button.setStyleSheet(self.button_style())
        self.csgo_launch_button.setFont(QFont("Montserrat", 12, QFont.Weight.ExtraBold))
        self.csgo_launch_button.setMinimumHeight(50)
        self.csgo_launch_button.clicked.connect(lambda: self.launch_game("csgo"))

        self.csgo_params_button = QPushButton()
        self.csgo_params_button.setStyleSheet(self.button_style())
        self.csgo_params_button.setFont(QFont("Montserrat", 12, QFont.Weight.ExtraBold))
        self.csgo_params_button.setMinimumHeight(50)
        self.csgo_params_button.clicked.connect(lambda: self.set_launch_params("csgo"))

        button_layout1 = QHBoxLayout()
        button_layout1.addWidget(self.csgo_boost_button)
        button_layout1.addWidget(self.csgo_launch_button)

        button_layout2 = QHBoxLayout()
        button_layout2.addWidget(self.csgo_discord_button)
        button_layout2.addWidget(self.csgo_local_files_button)

        csgo_layout.addLayout(button_layout1)
        csgo_layout.addLayout(button_layout2)
        csgo_layout.addWidget(self.csgo_params_button)

        # Ruta del juego
        self.csgo_path_label = QLabel()
        self.csgo_path_label.setStyleSheet(f"color: {self.text_color};")
        self.csgo_path_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        csgo_layout.addWidget(self.csgo_path_label)
        
        self.csgo_tab.setLayout(csgo_layout)

    def button_style(self):
        return (
            f"background-color: {self.button_color}; "
            "color: #0A0C0C; "
            "border-radius: 8px; "
            "padding: 10px;"
            "font-size: 14px;"
            "font-family: Montserrat;"
        )
        
    def apply_style(self):
        # Aplicar colores a la ventana principal
        self.setStyleSheet(f"background-color: {self.background_color};")
        
        # Actualizar estilos para todos los controles
        if hasattr(self, 'tabs'):
            self.tabs.setStyleSheet(f"""
                QTabWidget::pane {{ 
                    border: 1px solid #444; 
                    background-color: {self.background_color};
                }}
                QTabBar::tab {{ 
                    background-color: #222; 
                    color: {self.text_color}; 
                    padding: 8px 12px; 
                    margin-right: 2px; 
                }}
                QTabBar::tab:selected {{ 
                    background-color: {self.button_color}; 
                    color: #0A0C0C; 
                    font-weight: bold;
                }}
            """)
            
        if hasattr(self, 'welcome_label'):
            self.welcome_label.setStyleSheet(f"color: {self.text_color};")
            
        if hasattr(self, 'official_label'):
            self.official_label.setStyleSheet(f"background-color: {self.background_color}; color: {self.button_color}; font-weight: bold;")
            
        if hasattr(self, 'skin_selector_label'):
            self.skin_selector_label.setStyleSheet(f"background-color: {self.background_color}; color: {self.button_color}; font-weight: bold;")
            
        if hasattr(self, 'settings_label'):
            self.settings_label.setStyleSheet(f"background-color: {self.background_color}; color: {self.button_color}; font-weight: bold;")
            
        if hasattr(self, 'version_label'):
            self.version_label.setStyleSheet(f"color: {self.text_color};")
            
        if hasattr(self, 'madeby_label'):
            self.madeby_label.setStyleSheet(f"color: {self.text_color}; font-size: 8px; font-weight: bold;")
            
        if hasattr(self, 'language_label'):
            self.language_label.setStyleSheet(f"color: {self.text_color};")
            
        if hasattr(self, 'language_selector'):
            self.language_selector.setStyleSheet(f"color: {self.button_color};")
            
        # Actualizar estilos para CSSO tab
        if hasattr(self, 'csso_boost_button'):
            self.csso_boost_button.setStyleSheet(self.button_style())
            
        if hasattr(self, 'csso_discord_button'):
            self.csso_discord_button.setStyleSheet(self.button_style())
            
        if hasattr(self, 'csso_local_files_button'):
            self.csso_local_files_button.setStyleSheet(self.button_style())
            
        if hasattr(self, 'csso_launch_button'):
            self.csso_launch_button.setStyleSheet(self.button_style())
            
        if hasattr(self, 'csso_params_button'):
            self.csso_params_button.setStyleSheet(self.button_style())
            
        if hasattr(self, 'csso_path_label'):
            self.csso_path_label.setStyleSheet(f"color: {self.text_color};")
            
        # Actualizar estilos para CSGO tab
        if hasattr(self, 'csgo_boost_button'):
            self.csgo_boost_button.setStyleSheet(self.button_style())
            
        if hasattr(self, 'csgo_discord_button'):
            self.csgo_discord_button.setStyleSheet(self.button_style())
            
        if hasattr(self, 'csgo_local_files_button'):
            self.csgo_local_files_button.setStyleSheet(self.button_style())
            
        if hasattr(self, 'csgo_launch_button'):
            self.csgo_launch_button.setStyleSheet(self.button_style())
            
        if hasattr(self, 'csgo_params_button'):
            self.csgo_params_button.setStyleSheet(self.button_style())
            
        if hasattr(self, 'csgo_path_label'):
            self.csgo_path_label.setStyleSheet(f"color: {self.text_color};")

    def toggle_boost(self, game_type):
        if game_type == "csso":
            if not self.csso_game_path:
                self.csso_path_label.setText("⚠ Ruta del juego no establecida. Selecciona la carpeta del juego.")
                return

            self.csso_boost_enabled = not self.csso_boost_enabled

            csso_cfg_path = os.path.join(self.csso_game_path, "csso", "cfg")
            fpsboost_path = os.path.join(csso_cfg_path, "fpsboost.cfg")

            try:
                if self.csso_boost_enabled:
                    # Crear la carpeta cfg si no existe
                    os.makedirs(csso_cfg_path, exist_ok=True)
                    
                    # Copiar el archivo de configuración
                    with open(fpsboost_path, "w", encoding="utf-8") as f:
                        f.write(CSSO_FPSBOOST_CONFIG)

                    print(f"Archivo fpsboost.cfg creado en: {fpsboost_path}")

                    # Agregar parámetros del Boost
                    if " +exec fpsboost.cfg" not in self.csso_launch_params:
                        self.csso_launch_params += " +exec fpsboost.cfg"
                    self.csso_launch_params += f" {self.csso_custom_launch_params}"
                    print(f"CSSO Boost activado. Parámetros: {self.csso_launch_params}")
                else:
                    # Eliminar el archivo fpsboost.cfg si se desactiva el boost
                    if os.path.exists(fpsboost_path):
                        os.remove(fpsboost_path)
                        print(f"Archivo fpsboost.cfg eliminado de: {fpsboost_path}")

                    # Remover parámetros del Boost
                    self.csso_launch_params = self.csso_launch_params.replace(f" {self.csso_custom_launch_params}", "").replace(" +exec fpsboost.cfg", "").strip()
                    print(f"CSSO Boost desactivado. Parámetros actuales: {self.csso_launch_params}")
            except Exception as e:
                print(f"Error al gestionar el archivo fpsboost.cfg para CSSO: {e}")
                
        elif game_type == "csgo":
            if not self.csgo_game_path:
                self.csgo_path_label.setText("⚠ Ruta del juego no establecida. Selecciona la carpeta del juego.")
                return

            self.csgo_boost_enabled = not self.csgo_boost_enabled

            # Buscar la carpeta csgo/cfg dentro de la ruta del juego
            csgo_cfg_path = os.path.join(self.csgo_game_path, "csgo", "cfg")
            fpsboost_path = os.path.join(csgo_cfg_path, "fpsboost.cfg")

            try:
                if self.csgo_boost_enabled:
                    # Crear la carpeta cfg si no existe
                    os.makedirs(csgo_cfg_path, exist_ok=True)
                    
                    # Crear el archivo de configuración para CSGO
                    with open(fpsboost_path, "w", encoding="utf-8") as f:
                        f.write(CSGO_FPSBOOST_CONFIG)

                    print(f"Archivo fpsboost.cfg creado en: {fpsboost_path}")

                    # Agregar parámetros del Boost
                    if " +exec fpsboost.cfg" not in self.csgo_launch_params:
                        self.csgo_launch_params += " +exec fpsboost.cfg"
                    self.csgo_launch_params += f" {self.csgo_custom_launch_params}"
                    print(f"CSGO Boost activado. Parámetros: {self.csgo_launch_params}")
                else:
                    # Eliminar el archivo fpsboost.cfg si se desactiva el boost
                    if os.path.exists(fpsboost_path):
                        os.remove(fpsboost_path)
                        print(f"Archivo fpsboost.cfg eliminado de: {fpsboost_path}")

                    # Remover parámetros del Boost
                    self.csgo_launch_params = self.csgo_launch_params.replace(f" {self.csgo_custom_launch_params}", "").replace(" +exec fpsboost.cfg", "").strip()
                    print(f"CSGO Boost desactivado. Parámetros actuales: {self.csgo_launch_params}")
            except Exception as e:
                print(f"Error al gestionar el archivo fpsboost.cfg para CSGO: {e}")

        self.update_texts()
        self.save_config()
  
    def get_vpk_display_name(self, filename):
        # Si el archivo termina con .disabled, quitamos esa extensión para la visualización
        if filename.endswith('.vpk.disabled'):
            return filename[:-9]  # Quitar .disabled
        return filename

    def get_actual_vpk_name(self, display_name):
        # Recuperar el nombre real del archivo a partir del nombre mostrado
        if display_name.endswith('.vpk'):
            return display_name
        else:
            return f"{display_name}.disabled"

    def open_skin_selector(self):
        if not self.csso_game_path:
            self.csso_path_label.setText("⚠ Ruta del juego no establecida. Selecciona la carpeta del juego.")
            return
            
        custom_folder = os.path.join(self.csso_game_path, "csso", "custom")
        
        # Verificar si la carpeta custom existe
        if not os.path.exists(custom_folder):
            try:
                os.makedirs(custom_folder, exist_ok=True)
                print(f"Carpeta custom creada en: {custom_folder}")
            except Exception as e:
                print(f"Error al crear carpeta custom: {e}")
                return
        
        # Crear el diálogo del selector de skins
        dialog = QDialog(self)
        dialog.setWindowTitle(self.languages[self.current_language]["select_skins"])
        dialog.setStyleSheet(f"background-color: {self.background_color}; color: {self.text_color};")
        dialog.setMinimumWidth(400)
        dialog.setMinimumHeight(400)
        
        layout = QVBoxLayout()
        
        # Título
        title_label = QLabel(self.languages[self.current_language]["selected_vpks"])
        title_label.setStyleSheet(f"color: {self.button_color}; font-weight: bold; font-size: 14px;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        # Área desplazable para las casillas de verificación
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet(f"border: 1px solid {self.button_color};")
        
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        
        # Buscar archivos .vpk y .vpk.disabled en la carpeta custom
        vpk_files = []
        try:
            for file in os.listdir(custom_folder):
                if file.lower().endswith('.vpk') or file.lower().endswith('.vpk.disabled'):
                    vpk_files.append(file)
        except Exception as e:
            print(f"Error al listar archivos VPK: {e}")
        
        # Si no hay archivos VPK, mostrar un mensaje
        if not vpk_files:
            no_vpks_label = QLabel(self.languages[self.current_language]["no_vpks_found"])
            no_vpks_label.setStyleSheet(f"color: {self.text_color};")
            scroll_layout.addWidget(no_vpks_label)
        else:
            # Crear una casilla de verificación para cada archivo VPK
            self.vpk_checkboxes = {}
            for vpk_file in vpk_files:
                display_name = self.get_vpk_display_name(vpk_file)
                checkbox = QCheckBox(display_name)
                checkbox.setStyleSheet(f"color: {self.text_color};")
                
                # Verificar si el VPK está seleccionado (sin la extensión .disabled)
                if display_name in self.selected_vpks or vpk_file in self.selected_vpks:
                    checkbox.setChecked(True)
                
                self.vpk_checkboxes[display_name] = checkbox
                scroll_layout.addWidget(checkbox)
        
        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)
        layout.addWidget(scroll_area)
        
        # Botón de guardar
        save_button = QPushButton(self.languages[self.current_language]["save"])
        save_button.setStyleSheet(self.button_style())
        save_button.clicked.connect(lambda: self.save_skin_selection(dialog))
        layout.addWidget(save_button)
        
        dialog.setLayout(layout)
        dialog.exec()

    def apply_selected_vpks(self):
        if not self.csso_game_path:
            return
            
        custom_folder = os.path.join(self.csso_game_path, "csso", "custom")
        
        if not os.path.exists(custom_folder):
            try:
                os.makedirs(custom_folder, exist_ok=True)
            except Exception as e:
                print(f"Error al crear carpeta custom: {e}")
                return
                
        # Obtener todos los VPKs en la carpeta
        all_vpks = []
        try:
            for file in os.listdir(custom_folder):
                if file.lower().endswith('.vpk') or file.lower().endswith('.vpk.disabled'):
                    all_vpks.append(file)
        except Exception as e:
            print(f"Error al listar archivos VPK: {e}")
            return
        
        for vpk_file in all_vpks:
            vpk_path = os.path.join(custom_folder, vpk_file)
            base_name = self.get_vpk_display_name(vpk_file)
            
            # Si el VPK está en los seleccionados, renombramos para activarlo (quitando .disabled)
            if base_name in self.selected_vpks and vpk_file.endswith('.disabled'):
                new_path = vpk_path[:-9]  # Quitar .disabled
                try:
                    os.rename(vpk_path, new_path)
                    print(f"VPK activado: {vpk_file} -> {os.path.basename(new_path)}")
                except Exception as e:
                    print(f"Error al activar VPK {vpk_file}: {e}")
            
            # Si el VPK no está en los seleccionados y no está desactivado, lo desactivamos
            elif base_name not in self.selected_vpks and not vpk_file.endswith('.disabled'):
                new_path = f"{vpk_path}.disabled"
                try:
                    os.rename(vpk_path, new_path)
                    print(f"VPK desactivado: {vpk_file} -> {os.path.basename(new_path)}")
                except Exception as e:
                    print(f"Error al desactivar VPK {vpk_file}: {e}")

    def save_skin_selection(self, dialog):
        old_selected_vpks = self.selected_vpks.copy()
        self.selected_vpks = []
        
        # Recopilar los archivos VPK seleccionados por sus nombres mostrados
        if hasattr(self, 'vpk_checkboxes'):
            for display_name, checkbox in self.vpk_checkboxes.items():
                if checkbox.isChecked():
                    self.selected_vpks.append(display_name)
        
        # Solo aplicar cambios si la selección ha cambiado
        if set(old_selected_vpks) != set(self.selected_vpks):
            # Aplicar los cambios en los archivos VPK
            self.apply_selected_vpks()
            
        # Guardar la selección en la configuración
        self.save_config()
        
        # Mostrar mensaje de éxito
        QMessageBox.information(
            self, 
            self.languages[self.current_language]["select_skins"],
            self.languages[self.current_language]["skin_select_success"]
        )
        
        dialog.close()

    def open_link(self, url):
        webbrowser.open(url)

    def manage_game_path(self, game_type):
        if game_type == "csso":
            if self.csso_game_path:
                self.show_files_options_dialog(game_type)
            else:
                path = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta del Juego")
                if path:
                    self.csso_game_path = path
                    self.save_config()
                    self.update_texts()
        elif game_type == "csgo":
            if self.csgo_game_path:
                self.show_files_options_dialog(game_type)
            else:
                path = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta del Juego")
                if path:
                    self.csgo_game_path = path
                    self.save_config()
                    self.update_texts()
                    
    def show_files_options_dialog(self, game_type):
        game_path = self.csso_game_path if game_type == "csso" else self.csgo_game_path
        game_name = "CSSO" if game_type == "csso" else "CSGO"
        lang = self.languages[self.current_language]
        
        dialog = QDialog(self)
        dialog.setWindowTitle(f"{lang['local_files_options']} - {game_name}")
        dialog.setStyleSheet(f"background-color: {self.background_color}; color: {self.text_color};")
        dialog.setMinimumWidth(500)
        dialog.setMinimumHeight(400)
        
        layout = QVBoxLayout()
        
        # Título
        title_label = QLabel(f"{lang['local_files_management']} - {game_name}")
        title_label.setStyleSheet(f"color: {self.button_color}; font-weight: bold; font-size: 16px;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        # Botones de acciones
        button_layout = QVBoxLayout()
        
        # Botón para abrir carpeta principal
        open_main_button = QPushButton(f"{lang['open_main_folder']} {game_name}")
        open_main_button.setStyleSheet(self.button_style())
        open_main_button.clicked.connect(lambda: os.startfile(game_path))
        button_layout.addWidget(open_main_button)
        
        # Botón para abrir carpeta de configuración
        game_cfg_path = os.path.join(game_path, game_type.lower(), "cfg")
        open_cfg_button = QPushButton(lang['open_cfg_folder'])
        open_cfg_button.setStyleSheet(self.button_style())
        open_cfg_button.clicked.connect(lambda: self.safe_open_folder(game_cfg_path))
        button_layout.addWidget(open_cfg_button)
        
        # Botón para abrir carpeta custom (solo para CSSO)
        if game_type == "csso":
            game_custom_path = os.path.join(game_path, game_type.lower(), "custom")
            open_custom_button = QPushButton(lang['open_custom_folder'])
            open_custom_button.setStyleSheet(self.button_style())
            open_custom_button.clicked.connect(lambda: self.safe_open_folder(game_custom_path))
            button_layout.addWidget(open_custom_button)
        
        # Botón para crear respaldo
        backup_button = QPushButton(lang['create_config_backup'])
        backup_button.setStyleSheet(self.button_style())
        backup_button.clicked.connect(lambda: self.create_config_backup(game_type))
        button_layout.addWidget(backup_button)
        
        # Botón para restaurar respaldo
        restore_button = QPushButton(lang['restore_config_backup'])
        restore_button.setStyleSheet(self.button_style())
        restore_button.clicked.connect(lambda: self.restore_config_backup(game_type))
        button_layout.addWidget(restore_button)
        
        # Botón para cambiar ruta del juego
        change_path_button = QPushButton(lang['select_game_path'])
        change_path_button.setStyleSheet(self.button_style())
        change_path_button.clicked.connect(lambda: self.change_game_path(game_type, dialog))
        button_layout.addWidget(change_path_button)
        
        # Mostrar información de espacio en disco
        info_button = QPushButton(lang['show_disk_info'])
        info_button.setStyleSheet(self.button_style())
        info_button.clicked.connect(lambda: self.show_disk_info(game_path))
        button_layout.addWidget(info_button)
        
        layout.addLayout(button_layout)
        
        # Mostrar ruta actual
        path_label = QLabel(f"{lang['current_path']}: {game_path}")
        path_label.setStyleSheet(f"color: {self.text_color}; margin-top: 20px;")
        path_label.setWordWrap(True)
        layout.addWidget(path_label)
        
        # Botón de cerrar
        close_button = QPushButton(lang['close'])
        close_button.setStyleSheet(f"background-color: #666; color: {self.text_color}; border-radius: 8px; padding: 10px; margin-top: 20px;")
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        
        dialog.setLayout(layout)
        dialog.exec()

    def safe_open_folder(self, folder_path):
        """Abre una carpeta y la crea si no existe."""
        lang = self.languages[self.current_language]
        try:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path, exist_ok=True)
                print(f"Carpeta creada: {folder_path}")
            os.startfile(folder_path)
        except Exception as e:
            QMessageBox.warning(self, lang["error"], f"{lang['folder_error']} {str(e)}")

    def create_config_backup(self, game_type):
        """Crea un respaldo de los archivos de configuración."""
        lang = self.languages[self.current_language]
        try:
            game_path = self.csso_game_path if game_type == "csso" else self.csgo_game_path
            cfg_path = os.path.join(game_path, game_type.lower(), "cfg")
            
            # Crear carpeta de respaldos si no existe
            backup_dir = os.path.join(CONFIG_DIR, f"{game_type}_backups")
            os.makedirs(backup_dir, exist_ok=True)
            
            # Nombre del archivo con timestamp
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = os.path.join(backup_dir, f"{game_type}_cfg_backup_{timestamp}.zip")
            
            # Verificar si hay archivos para respaldar
            if not os.path.exists(cfg_path) or not os.listdir(cfg_path):
                QMessageBox.information(self, lang["info"], lang["no_files_to_backup"])
                return
            
            # Crear archivo ZIP
            import zipfile
            with zipfile.ZipFile(backup_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(cfg_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.relpath(file_path, cfg_path))
            
            QMessageBox.information(self, lang["success"], f"{lang['backup_created']}\n{backup_file}")
        except Exception as e:
            QMessageBox.warning(self, lang["error"], f"{lang['error']}: {str(e)}")

    def restore_config_backup(self, game_type):
        """Restaura un respaldo de configuración."""
        lang = self.languages[self.current_language]
        try:
            # Directorio de respaldos
            backup_dir = os.path.join(CONFIG_DIR, f"{game_type}_backups")
            if not os.path.exists(backup_dir) or not os.listdir(backup_dir):
                QMessageBox.information(self, lang["info"], lang["no_backups"])
                return
            
            # Mostrar diálogo para seleccionar archivo de respaldo
            backup_file, _ = QFileDialog.getOpenFileName(
                self, lang["restore_config_backup"],
                backup_dir, "Archivos ZIP (*.zip)"
            )
            
            if not backup_file:
                return
            
            # Confirmar restauración
            confirm = QMessageBox.question(
                self, lang["info"], 
                lang["confirm_restore"],
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            
            if confirm == QMessageBox.StandardButton.Yes:
                game_path = self.csso_game_path if game_type == "csso" else self.csgo_game_path
                cfg_path = os.path.join(game_path, game_type.lower(), "cfg")
                
                # Crear directorio cfg si no existe
                os.makedirs(cfg_path, exist_ok=True)
                
                # Extraer archivo ZIP
                import zipfile
                with zipfile.ZipFile(backup_file, 'r') as zipf:
                    zipf.extractall(cfg_path)
                
                QMessageBox.information(self, lang["success"], lang["backup_restored"])
        except Exception as e:
            QMessageBox.warning(self, lang["error"], f"{lang['error']}: {str(e)}")

    def change_game_path(self, game_type, parent_dialog=None):
        """Cambia la ruta del juego."""
        lang = self.languages[self.current_language]
        path = QFileDialog.getExistingDirectory(self, f"{lang['select_game_path']} {game_type.upper()}")
        if path:
            if game_type == "csso":
                self.csso_game_path = path
            else:
                self.csgo_game_path = path
            
            self.save_config()
            self.update_texts()
            
            QMessageBox.information(self, lang["success"], f"{lang['path_updated']}")
            
            # Cerrar el diálogo padre si existe
            if parent_dialog:
                parent_dialog.close()

    def show_disk_info(self, path):
        """Muestra información sobre el espacio en disco."""
        lang = self.languages[self.current_language]
        try:
            import shutil
            
            # Obtener información del disco
            total, used, free = shutil.disk_usage(path)
            
            # Convertir a formato legible
            def format_size(size_bytes):
                for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                    if size_bytes < 1024 or unit == 'TB':
                        return f"{size_bytes:.2f} {unit}"
                    size_bytes /= 1024
            
            # Calcular porcentaje usado
            percent_used = (used / total) * 100
            
            # Construir mensaje
            message = f"{lang['disk_info']}\n{path}\n\n"
            message += f"{lang['total_space']} {format_size(total)}\n"
            message += f"{lang['used_space']} {format_size(used)} ({percent_used:.1f}%)\n"
            message += f"{lang['free_space']} {format_size(free)} ({100-percent_used:.1f}%)\n"
            
            # Mostrar advertencia si queda poco espacio
            if percent_used > 90:
                message += f"\n{lang['disk_warning']}"
            
            QMessageBox.information(self, lang["disk_info"], message)
        except Exception as e:
            QMessageBox.warning(self, lang["error"], f"{lang['disk_info_error']} {str(e)}")

    def launch_game(self, game_type):
        if game_type == "csso":
            if self.csso_game_path:
                os.system(f'"{self.csso_game_path}/hl2.exe" {self.csso_launch_params}')
            else:
                self.update_texts()
        elif game_type == "csgo":
            if self.csgo_game_path:
                # Para CSGO usamos csgo.exe en lugar de hl2.exe
                os.system(f'"{self.csgo_game_path}/csgo.exe" {self.csgo_launch_params}')
            else:
                self.update_texts()

    def set_launch_params(self, game_type):
        dialog = QDialog(self)
        dialog.setWindowTitle(self.languages[self.current_language]["launch_params"])
        dialog.setStyleSheet(f"background-color: {self.background_color}; color: {self.text_color};")
        layout = QVBoxLayout()

        param_input = QTextEdit()
        param_input.setFont(QFont("Montserrat", 12, QFont.Weight.ExtraBold))
        param_input.setStyleSheet(f"background-color: #222; color: {self.text_color}; border: 1px solid #444;")
        
        if game_type == "csso":
            param_input.setText(self.csso_launch_params)
        elif game_type == "csgo":
            param_input.setText(self.csgo_launch_params)

        save_button = QPushButton(self.languages[self.current_language]["save"])
        save_button.setStyleSheet(self.button_style())
        save_button.setFont(QFont("Montserrat", 12, QFont.Weight.ExtraBold))
        save_button.clicked.connect(lambda: self.save_params(dialog, param_input, game_type))

        layout.addWidget(param_input)
        layout.addWidget(save_button)
        dialog.setLayout(layout)
        dialog.exec()

    def save_params(self, dialog, param_input, game_type):
        if game_type == "csso":
            self.csso_launch_params = param_input.toPlainText()
        elif game_type == "csgo":
            self.csgo_launch_params = param_input.toPlainText()
        
        dialog.close()
        self.save_config()

    def change_language(self, lang):
        self.current_language = lang
        self.update_texts()
        self.save_config()

    def open_settings(self):
        dialog = QDialog(self)
        dialog.setWindowTitle(self.languages[self.current_language]["settings_title"])
        dialog.setStyleSheet(f"background-color: {self.background_color}; color: {self.text_color};")
        dialog.setMinimumWidth(400)
        layout = QVBoxLayout()

        # Sección de nombre de usuario
        username_label = QLabel(self.languages[self.current_language]["username"])
        username_label.setStyleSheet(f"color: {self.text_color}; font-weight: bold;")
        layout.addWidget(username_label)

        username_input = QLineEdit()
        username_input.setFont(QFont("Montserrat", 12))
        username_input.setText(self.user_name)
        username_input.setStyleSheet(f"background-color: #222; color: {self.text_color}; border: 1px solid #444; padding: 5px;")
        layout.addWidget(username_input)
        layout.addSpacing(15)

        # Sección de color de fondo
        bg_color_label = QLabel(self.languages[self.current_language]["background_color"])
        bg_color_label.setStyleSheet(f"color: {self.text_color}; font-weight: bold;")
        layout.addWidget(bg_color_label)

        bg_color_layout = QHBoxLayout()
        bg_color_preview = QFrame()
        bg_color_preview.setFixedSize(30, 30)
        bg_color_preview.setStyleSheet(f"background-color: {self.background_color}; border: 1px solid #888;")
        
        bg_color_button = QPushButton(self.languages[self.current_language]["choose_color"])
        bg_color_button.setStyleSheet(self.button_style())
        bg_color_button.clicked.connect(lambda: self.choose_color("background", bg_color_preview))
        
        bg_color_layout.addWidget(bg_color_preview)
        bg_color_layout.addWidget(bg_color_button)
        layout.addLayout(bg_color_layout)
        layout.addSpacing(15)

        # Sección de color de botones
        button_color_label = QLabel(self.languages[self.current_language]["button_color"])
        button_color_label.setStyleSheet(f"color: {self.text_color}; font-weight: bold;")
        layout.addWidget(button_color_label)

        button_color_layout = QHBoxLayout()
        button_color_preview = QFrame()
        button_color_preview.setFixedSize(30, 30)
        button_color_preview.setStyleSheet(f"background-color: {self.button_color}; border: 1px solid #888;")
        
        button_color_button = QPushButton(self.languages[self.current_language]["choose_color"])
        button_color_button.setStyleSheet(self.button_style())
        button_color_button.clicked.connect(lambda: self.choose_color("button", button_color_preview))
        
        button_color_layout.addWidget(button_color_preview)
        button_color_layout.addWidget(button_color_button)
        layout.addLayout(button_color_layout)
        layout.addSpacing(15)

        # Sección de color de texto
        text_color_label = QLabel(self.languages[self.current_language]["text_color"])
        text_color_label.setStyleSheet(f"color: {self.text_color}; font-weight: bold;")
        layout.addWidget(text_color_label)

        text_color_layout = QHBoxLayout()
        text_color_preview = QFrame()
        text_color_preview.setFixedSize(30, 30)
        text_color_preview.setStyleSheet(f"background-color: {self.text_color}; border: 1px solid #888;")
        
        text_color_button = QPushButton(self.languages[self.current_language]["choose_color"])
        text_color_button.setStyleSheet(self.button_style())
        text_color_button.clicked.connect(lambda: self.choose_color("text", text_color_preview))
        
        text_color_layout.addWidget(text_color_preview)
        text_color_layout.addWidget(text_color_button)
        layout.addLayout(text_color_layout)
        layout.addSpacing(15)

        # Botón para restablecer colores predeterminados
        reset_colors_button = QPushButton(self.languages[self.current_language]["reset_colors"])
        reset_colors_button.setStyleSheet(self.button_style())
        reset_colors_button.clicked.connect(lambda: self.reset_colors(bg_color_preview, button_color_preview, text_color_preview))
        layout.addWidget(reset_colors_button)
        layout.addSpacing(20)

        # Botones de acción
        buttons_layout = QHBoxLayout()
        
        cancel_button = QPushButton(self.languages[self.current_language]["cancel"])
        cancel_button.setStyleSheet(f"background-color: #666; color: {self.text_color}; border-radius: 8px; padding: 10px;")
        cancel_button.clicked.connect(dialog.reject)
        
        apply_button = QPushButton(self.languages[self.current_language]["apply"])
        apply_button.setStyleSheet(self.button_style())
        apply_button.clicked.connect(lambda: self.save_settings(dialog, username_input))
        
        buttons_layout.addWidget(cancel_button)
        buttons_layout.addWidget(apply_button)
        layout.addLayout(buttons_layout)

        dialog.setLayout(layout)
        dialog.exec()

    def choose_color(self, color_type, preview_widget):
        color = QColorDialog.getColor()
        if color.isValid():
            hex_color = color.name()
            preview_widget.setStyleSheet(f"background-color: {hex_color}; border: 1px solid #888;")
            
            if color_type == "background":
                self.background_color = hex_color
            elif color_type == "button":
                self.button_color = hex_color
            elif color_type == "text":
                self.text_color = hex_color

    def reset_colors(self, bg_preview, button_preview, text_preview):
        # Restablecer colores predeterminados
        self.background_color = "#0A0C0C"
        self.button_color = "#E14A00"
        self.text_color = "#EBEFF3"
        
        # Actualizar previsualizaciones
        bg_preview.setStyleSheet(f"background-color: {self.background_color}; border: 1px solid #888;")
        button_preview.setStyleSheet(f"background-color: {self.button_color}; border: 1px solid #888;")
        text_preview.setStyleSheet(f"background-color: {self.text_color}; border: 1px solid #888;")

    def save_settings(self, dialog, username_input):
        # Guardar el nuevo nombre de usuario
        self.user_name = username_input.text()
        
        # Aplicar los nuevos colores
        self.apply_style()
        
        # Actualizar textos
        self.update_texts()
        
        # Guardar en configuración
        self.save_config()
        
        dialog.accept()

    def update_texts(self):
        lang = self.languages[self.current_language]
        
        # Actualizar pestañas
        self.tabs.setTabText(0, lang["csso_tab"])
        self.tabs.setTabText(1, lang["csgo_tab"])
        
        # Actualizar textos comunes
        self.welcome_label.setText(f"{lang['welcome']}, <span style='color: {self.button_color};'>{self.user_name}</span>")
        self.version_label.setText(lang["version"].replace("#E14A00", self.button_color).replace("#EBEFF3", self.text_color))
        
        # Configurar textos con formato HTML
        self.official_label.setText(f"<span style='color: {self.button_color};'>{lang['official_page'].split()[0]}</span> <span style='color: {self.text_color};'>{lang['official_page'].split()[1]}</span>")
        
        # Texto completo para el selector de skins
        self.skin_selector_label.setText(lang["report_errors"])
        
        self.settings_label.setText(f"<span style='color: {self.button_color};'>{lang['settings'].split()[0] if ' ' in lang['settings'] else lang['settings']}</span>")

        # Actualizar etiqueta de idioma
        self.language_label.setText(lang["language_text"])
        
        # Actualizar textos de CSSO
        self.csso_boost_button.setText(lang["boost"] if not self.csso_boost_enabled else lang["disable_boost"])
        self.csso_discord_button.setText(lang["discord"])
        self.csso_local_files_button.setText(lang["local_files"])
        self.csso_launch_button.setText(lang["launch_game"])
        self.csso_params_button.setText(lang["launch_params"])
        self.csso_path_label.setText(
            lang["game_path_not_set"] if not self.csso_game_path else f"{lang['game_path']}: {self.csso_game_path}"
        )
        
        # Actualizar textos de CSGO
        self.csgo_boost_button.setText(lang["boost"] if not self.csgo_boost_enabled else lang["disable_boost"])
        self.csgo_discord_button.setText(lang["discord"])
        self.csgo_local_files_button.setText(lang["local_files"])
        self.csgo_launch_button.setText(lang["launch_game"])
        self.csgo_params_button.setText(lang["launch_params"])
        self.csgo_path_label.setText(
            lang["game_path_not_set"] if not self.csgo_game_path else f"{lang['game_path']}: {self.csgo_game_path}"
        )

    def save_config(self):
        config = {
            "csso_game_path": self.csso_game_path,
            "csso_launch_params": self.csso_launch_params,
            "csso_boost_enabled": self.csso_boost_enabled,
            "csgo_game_path": self.csgo_game_path,
            "csgo_launch_params": self.csgo_launch_params,
            "csgo_boost_enabled": self.csgo_boost_enabled,
            "user_name": self.user_name,
            "current_language": self.current_language,
            "selected_vpks": self.selected_vpks,   # Guardar VPKs seleccionados (solo para CSSO)
            "background_color": self.background_color,
            "button_color": self.button_color,
            "text_color": self.text_color
        }
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f)

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                try:
                    config = json.load(f)
                    
                    # Configuración para CSSO
                    self.csso_game_path = config.get("csso_game_path")
                    self.csso_launch_params = config.get("csso_launch_params", "-game csso -insecure")
                    self.csso_boost_enabled = config.get("csso_boost_enabled", False)
                    self.selected_vpks = config.get("selected_vpks", [])  # Cargar VPKs seleccionados
                    
                    # Verificar que csso_launch_params tenga el valor correcto si el boost está activado
                    if self.csso_boost_enabled and " +exec fpsboost.cfg" not in self.csso_launch_params:
                        self.csso_launch_params += " +exec fpsboost.cfg"
                    if self.csso_boost_enabled and self.csso_custom_launch_params not in self.csso_launch_params:
                        self.csso_launch_params += f" {self.csso_custom_launch_params}"
                    
                    # Configuración para CSGO
                    self.csgo_game_path = config.get("csgo_game_path")
                    self.csgo_launch_params = config.get("csgo_launch_params", "-steam -silent")
                    self.csgo_boost_enabled = config.get("csgo_boost_enabled", False)
                    
                    # Verificar que csgo_launch_params tenga el valor correcto si el boost está activado
                    if self.csgo_boost_enabled and " +exec fpsboost.cfg" not in self.csgo_launch_params:
                        self.csgo_launch_params += " +exec fpsboost.cfg"
                    if self.csgo_boost_enabled and self.csgo_custom_launch_params not in self.csgo_launch_params:
                        self.csgo_launch_params += f" {self.csgo_custom_launch_params}"
                    
                    # Configuración general
                    self.user_name = config.get("user_name", "User")
                    self.current_language = config.get("current_language", "Es")
                    
                    # Cargar colores personalizados
                    self.background_color = config.get("background_color", "#0A0C0C")
                    self.button_color = config.get("button_color", "#E14A00")
                    self.text_color = config.get("text_color", "#EBEFF3")
                    
                except Exception as e:
                    print(f"Error al cargar la configuración: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    launcher = LauncherApp()
    launcher.resize(600, 400)
    launcher.show()
    sys.exit(app.exec())