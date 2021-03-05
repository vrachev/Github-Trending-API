"""Allowed Parameters
===================
path and query parameters which are allowed to use.
"""
# Copyright (c) 2021, Niklas Tiede.
# All rights reserved. Distributed under the MIT License.

from enum import Enum


class AllowedDateRanges(str, Enum):
    """ optional query parameter, default date range: daily """
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"


class AllowedSpokenLanguages(str, Enum):
    """ optional query parameter, default language: any 
    identifier (language name) = 2-char-string (abbrev. for urlParam)
    """
    Abkhazian = 'ab'
    Afar = 'aa'
    Afrikaans = 'af'
    Akan = 'ak'
    Albanian = 'sq'
    Amharic = 'am'
    Arabic = 'ar'
    Aragonese = 'an'
    Armenian = 'hy'
    Assamese = 'as'
    Avaric = 'av'
    Avestan = 'ae'
    Aymara = 'ay'
    Azerbaijani = 'az'
    Bambara = 'bm'
    Bashkir = 'ba'
    Basque = 'eu'
    Belarusian = 'be'
    Bengali = 'bn'
    Bihari_languages = 'bh'
    Bislama = 'bi'
    Bosnian = 'bs'
    Breton = 'br'
    Bulgarian = 'bg'
    Burmese = 'my'
    Catalan_Valencian = 'ca'
    Chamorro = 'ch'
    Chechen = 'ce'
    Chichewa_Chewa_Nyanja = 'ny'
    Chinese = 'zh'
    Chuvash = 'cv'
    Cornish = 'kw'
    Corsican = 'co'
    Cree = 'cr'
    Croatian = 'hr'
    Czech = 'cs'
    Danish = 'da'
    Divehi_Dhivehi_Maldivian = 'dv'
    Dutch_Flemish = 'nl'
    Dzongkha = 'dz'
    English = 'en'
    Esperanto = 'eo'
    Estonian = 'et'
    Ewe = 'ee'
    Faroese = 'fo'
    Fijian = 'fj'
    Finnish = 'fi'
    French = 'fr'
    Fulah = 'ff'
    Galician = 'gl'
    Georgian = 'ka'
    German = 'de'
    Greek_Modern = 'el'
    Guarani = 'gn'
    Gujarati = 'gu'
    Haitian_Haitian_Creole = 'ht'
    Hausa = 'ha'
    Hebrew = 'he'
    Herero = 'hz'
    Hindi = 'hi'
    Hiri_Motu = 'ho'
    Hungarian = 'hu'
    Interlingua_International_Auxil = 'ia'
    Indonesian = 'id'
    Interlingue_Occidental = 'ie'
    Irish = 'ga'
    Igbo = 'ig'
    Inupiaq = 'ik'
    Ido = 'io'
    Icelandic = 'is'
    Italian = 'it'
    Inuktitut = 'iu'
    Japanese = 'ja'
    Javanese = 'jv'
    Kalaallisut_Greenlandic = 'kl'
    Kannada = 'kn'
    Kanuri = 'kr'
    Kashmiri = 'ks'
    Kazakh = 'kk'
    Central_Khmer = 'km'
    Kikuyu_Gikuyu = 'ki'
    Kinyarwanda = 'rw'
    Kirghiz_Kyrgyz = 'ky'
    Komi = 'kv'
    Kongo = 'kg'
    Korean = 'ko'
    Kurdish = 'ku'
    Kuanyama_Kwanyama = 'kj'
    Latin = 'la'
    Luxembourgish_Letzeburgesch = 'lb'
    Ganda = 'lg'
    Limburgan_Limburger_Limburgish = 'li'
    Lingala = 'ln'
    Lao = 'lo'
    Lithuanian = 'lt'
    Luba_Katanga = 'lu'
    Latvian = 'lv'
    Manx = 'gv'
    Macedonian = 'mk'
    Malagasy = 'mg'
    Malay = 'ms'
    Malayalam = 'ml'
    Maltese = 'mt'
    Maori = 'mi'
    Marathi = 'mr'
    Marshallese = 'mh'
    Mongolian = 'mn'
    Nauru = 'na'
    Navajo_Navaho = 'nv'
    North_Ndebele = 'nd'
    Nepali = 'ne'
    Ndonga = 'ng'
    Norwegian_Bokmål = 'nb'
    Norwegian_Nynorsk = 'nn'
    Norwegian = 'no'
    Sichuan_Yi_Nuosu = 'ii'
    South_Ndebele = 'nr'
    Occitan = 'oc'
    Ojibwa = 'oj'
    Church_Slavic_Old_Slavonic_Chu = 'cu'
    Oromo = 'om'
    Oriya = 'or'
    Ossetian_Ossetic = 'os'
    Punjabi_Panjabi = 'pa'
    Pali = 'pi'
    Persian = 'fa'
    Polish = 'pl'
    Pashto_Pushto = 'ps'
    Portuguese = 'pt'
    Quechua = 'qu'
    Romansh = 'rm'
    Rundi = 'rn'
    Romanian_Moldavian_Moldovan = 'ro'
    Russian = 'ru'
    Sanskrit = 'sa'
    Sardinian = 'sc'
    Sindhi = 'sd'
    Northern_Sami = 'se'
    Samoan = 'sm'
    Sango = 'sg'
    Serbian = 'sr'
    Gaelic_Scottish_Gaelic = 'gd'
    Shona = 'sn'
    Sinhala_Sinhalese = 'si'
    Slovak = 'sk'
    Slovenian = 'sl'
    Somali = 'so'
    Southern_Sotho = 'st'
    Spanish_Castilian = 'es'
    Sundanese = 'su'
    Swahili = 'sw'
    Swati = 'ss'
    Swedish = 'sv'
    Tamil = 'ta'
    Telugu = 'te'
    Tajik = 'tg'
    Thai = 'th'
    Tigrinya = 'ti'
    Tibetan = 'bo'
    Turkmen = 'tk'
    Tagalog = 'tl'
    Tswana = 'tn'
    Tonga_Tonga_Islands = 'to'
    Turkish = 'tr'
    Tsonga = 'ts'
    Tatar = 'tt'
    Twi = 'tw'
    Tahitian = 'ty'
    Uighur_Uyghur = 'ug'
    Ukrainian = 'uk'
    Urdu = 'ur'
    Uzbek = 'uz'
    Venda = 've'
    Vietnamese = 'vi'
    Volapük = 'vo'
    Walloon = 'wa'
    Welsh = 'cy'
    Wolof = 'wo'
    Western_Frisian = 'fy'
    Xhosa = 'xh'
    Yiddish = 'yi'
    Yoruba = 'yo'
    Zhuang_Chuang = 'za'
    Zulu = 'zu'


class AllowedProgrammingLanguages(str, Enum):
    """ Path Parameter 
    identifier (language name) = string (urlParam)
    """
    c__ = "c++"
    html = "html"
    javascript = "javascript"
    jupyter_notebook = "jupyter-notebook"
    python = "python"
    shell = "shell"
    typescript = "typescript"
    unknown = "unknown"
    _1c_enterprise = "1c-enterprise"
    _4d = "4d"
    abap = "abap"
    abap_cds = "abap-cds"
    abnf = "abnf"
    actionscript = "actionscript"
    ada = "ada"
    adobe_font_metrics = "adobe-font-metrics"
    agda = "agda"
    ags_script = "ags-script"
    al = "al"
    alloy = "alloy"
    alpine_abuild = "alpine-abuild"
    altium_designer = "altium-designer"
    ampl = "ampl"
    angelscript = "angelscript"
    ant_build_system = "ant-build-system"
    antlr = "antlr"
    apacheconf = "apacheconf"
    apex = "apex"
    api_blueprint = "api-blueprint"
    apl = "apl"
    apollo_guidance_computer = "apollo-guidance-computer"
    applescript = "applescript"
    arc = "arc"
    asciidoc = "asciidoc"
    asl = "asl"
    asn1 = "asn.1"
    classic_asp = "classic-asp"
    aspnet = "asp.net"
    aspectj = "aspectj"
    assembly = "assembly"
    asymptote = "asymptote"
    ats = "ats"
    augeas = "augeas"
    autohotkey = "autohotkey"
    autoit = "autoit"
    avro_idl = "avro-idl"
    awk = "awk"
    ballerina = "ballerina"
    batchfile = "batchfile"
    beef = "beef"
    befunge = "befunge"
    bibtex = "bibtex"
    bison = "bison"
    bitbake = "bitbake"
    blade = "blade"
    blitzbasic = "blitzbasic"
    blitzmax = "blitzmax"
    bluespec = "bluespec"
    boo = "boo"
    boogie = "boogie"
    brainfuck = "brainfuck"
    brightscript = "brightscript"
    c = "c"
    c_23 = "c%23"
    c_objdump = "c-objdump"
    c2hs_haskell = "c2hs-haskell"
    cabal_config = "cabal-config"
    capn_proto = "cap'n-proto"
    cartocss = "cartocss"
    ceylon = "ceylon"
    chapel = "chapel"
    charity = "charity"
    chuck = "chuck"
    cirru = "cirru"
    clarion = "clarion"
    clean = "clean"
    click = "click"
    clips = "clips"
    clojure = "clojure"
    closure_templates = "closure-templates"
    cloud_firestore_security_rules = "cloud-firestore-security-rules"
    cmake = "cmake"
    cobol = "cobol"
    codeql = "codeql"
    coffeescript = "coffeescript"
    coldfusion = "coldfusion"
    coldfusion_cfc = "coldfusion-cfc"
    collada = "collada"
    common_lisp = "common-lisp"
    common_workflow_language = "common-workflow-language"
    component_pascal = "component-pascal"
    conll_u = "conll-u"
    cool = "cool"
    coq = "coq"
    cpp_objdump = "cpp-objdump"
    creole = "creole"
    crystal = "crystal"
    cson = "cson"
    csound = "csound"
    csound_document = "csound-document"
    csound_score = "csound-score"
    css = "css"
    csv = "csv"
    cuda = "cuda"
    curl_config = "curl-config"
    cweb = "cweb"
    cycript = "cycript"
    cython = "cython"
    d = "d"
    d_objdump = "d-objdump"
    dafny = "dafny"
    darcs_patch = "darcs-patch"
    dart = "dart"
    dataweave = "dataweave"
    desktop = "desktop"
    dhall = "dhall"
    diff = "diff"
    digital_command_language = "digital-command-language"
    dircolors = "dircolors"
    directx_3d_file = "directx-3d-file"
    dm = "dm"
    dns_zone = "dns-zone"
    dockerfile = "dockerfile"
    dogescript = "dogescript"
    dtrace = "dtrace"
    dylan = "dylan"
    e = "e"
    eagle = "eagle"
    easybuild = "easybuild"
    ebnf = "ebnf"
    ec = "ec"
    ecere_projects = "ecere-projects"
    ecl = "ecl"
    eclipse = "eclipse"
    editorconfig = "editorconfig"
    edje_data_collection = "edje-data-collection"
    edn = "edn"
    eiffel = "eiffel"
    ejs = "ejs"
    elixir = "elixir"
    elm = "elm"
    emacs_lisp = "emacs-lisp"
    emberscript = "emberscript"
    eml = "eml"
    eq = "eq"
    erlang = "erlang"
    f_23 = "f%23"
    f_ = "f*"
    factor = "factor"
    fancy = "fancy"
    fantom = "fantom"
    faust = "faust"
    figlet_font = "figlet-font"
    filebench_wml = "filebench-wml"
    filterscript = "filterscript"
    fish = "fish"
    flux = "flux"
    formatted = "formatted"
    forth = "forth"
    fortran = "fortran"
    fortran_free_form = "fortran-free-form"
    freemarker = "freemarker"
    frege = "frege"
    futhark = "futhark"
    g_code = "g-code"
    game_maker_language = "game-maker-language"
    gaml = "gaml"
    gams = "gams"
    gap = "gap"
    gcc_machine_description = "gcc-machine-description"
    gdb = "gdb"
    gdscript = "gdscript"
    gedcom = "gedcom"
    genie = "genie"
    genshi = "genshi"
    gentoo_ebuild = "gentoo-ebuild"
    gentoo_eclass = "gentoo-eclass"
    gerber_image = "gerber-image"
    gettext_catalog = "gettext-catalog"
    gherkin = "gherkin"
    git_attributes = "git-attributes"
    git_config = "git-config"
    glsl = "glsl"
    glyph = "glyph"
    glyph_bitmap_distribution_format = "glyph-bitmap-distribution-format"
    gn = "gn"
    gnuplot = "gnuplot"
    go = "go"
    golo = "golo"
    gosu = "gosu"
    grace = "grace"
    gradle = "gradle"
    grammatical_framework = "grammatical-framework"
    graph_modeling_language = "graph-modeling-language"
    graphql = "graphql"
    graphviz_dot = "graphviz-(dot)"
    groovy = "groovy"
    groovy_server_pages = "groovy-server-pages"
    hack = "hack"
    haml = "haml"
    handlebars = "handlebars"
    haproxy = "haproxy"
    harbour = "harbour"
    haskell = "haskell"
    haxe = "haxe"
    hcl = "hcl"
    hiveql = "hiveql"
    hlsl = "hlsl"
    holyc = "holyc"
    html_django = "html+django"
    html_ecr = "html+ecr"
    html_eex = "html+eex"
    html_erb = "html+erb"
    html_php = "html+php"
    html_razor = "html+razor"
    http = "http"
    hxml = "hxml"
    hy = "hy"
    hyphy = "hyphy"
    idl = "idl"
    idris = "idris"
    ignore_list = "ignore-list"
    igor_pro = "igor-pro"
    imagej_macro = "imagej-macro"
    inform_7 = "inform-7"
    ini = "ini"
    inno_setup = "inno-setup"
    io = "io"
    ioke = "ioke"
    irc_log = "irc-log"
    isabelle = "isabelle"
    isabelle_root = "isabelle-root"
    j = "j"
    jasmin = "jasmin"
    java = "java"
    java_properties = "java-properties"
    java_server_pages = "java-server-pages"
    javascript_erb = "javascript+erb"
    jflex = "jflex"
    jison = "jison"
    jison_lex = "jison-lex"
    jolie = "jolie"
    json = "json"
    json_with_comments = "json-with-comments"
    json5 = "json5"
    jsoniq = "jsoniq"
    jsonld = "jsonld"
    jsonnet = "jsonnet"
    julia = "julia"
    kaitai_struct = "kaitai-struct"
    kicad_layout = "kicad-layout"
    kicad_legacy_layout = "kicad-legacy-layout"
    kicad_schematic = "kicad-schematic"
    kit = "kit"
    kotlin = "kotlin"
    krl = "krl"
    labview = "labview"
    lasso = "lasso"
    latte = "latte"
    lean = "lean"
    less = "less"
    lex = "lex"
    lfe = "lfe"
    lilypond = "lilypond"
    limbo = "limbo"
    linker_script = "linker-script"
    linux_kernel_module = "linux-kernel-module"
    liquid = "liquid"
    literate_agda = "literate-agda"
    literate_coffeescript = "literate-coffeescript"
    literate_haskell = "literate-haskell"
    livescript = "livescript"
    llvm = "llvm"
    logos = "logos"
    logtalk = "logtalk"
    lolcode = "lolcode"
    lookml = "lookml"
    loomscript = "loomscript"
    lsl = "lsl"
    ltspice_symbol = "ltspice-symbol"
    lua = "lua"
    m = "m"
    m4 = "m4"
    m4sugar = "m4sugar"
    macaulay2 = "macaulay2"
    makefile = "makefile"
    mako = "mako"
    markdown = "markdown"
    marko = "marko"
    mask = "mask"
    mathematica = "mathematica"
    matlab = "matlab"
    maven_pom = "maven-pom"
    _max = "max"
    maxscript = "maxscript"
    mcfunction = "mcfunction"
    mediawiki = "mediawiki"
    mercury = "mercury"
    meson = "meson"
    metal = "metal"
    microsoft_developer_studio_project = "microsoft-developer-studio-project"
    minid = "minid"
    mirah = "mirah"
    mirc_script = "mirc-script"
    mlir = "mlir"
    modelica = "modelica"
    modula_2 = "modula-2"
    modula_3 = "modula-3"
    module_management_system = "module-management-system"
    monkey = "monkey"
    moocode = "moocode"
    moonscript = "moonscript"
    motorola_68k_assembly = "motorola-68k-assembly"
    mql4 = "mql4"
    mql5 = "mql5"
    mtml = "mtml"
    muf = "muf"
    mupad = "mupad"
    muse = "muse"
    mustache = "mustache"
    myghty = "myghty"
    nanorc = "nanorc"
    nasl = "nasl"
    ncl = "ncl"
    nearley = "nearley"
    nemerle = "nemerle"
    nesc = "nesc"
    netlinx = "netlinx"
    netlinx_erb = "netlinx+erb"
    netlogo = "netlogo"
    newlisp = "newlisp"
    nextflow = "nextflow"
    nginx = "nginx"
    nim = "nim"
    ninja = "ninja"
    nit = "nit"
    nix = "nix"
    nl = "nl"
    npm_config = "npm-config"
    nsis = "nsis"
    nu = "nu"
    numpy = "numpy"
    nunjucks = "nunjucks"
    nwscript = "nwscript"
    objdump = "objdump"
    object_data_instance_notation = "object-data-instance-notation"
    objective_c = "objective-c"
    objective_c__ = "objective-c++"
    objective_j = "objective-j"
    objectscript = "objectscript"
    ocaml = "ocaml"
    odin = "odin"
    omgrofl = "omgrofl"
    ooc = "ooc"
    opa = "opa"
    opal = "opal"
    open_policy_agent = "open-policy-agent"
    opencl = "opencl"
    openedge_abl = "openedge-abl"
    openqasm = "openqasm"
    openrc_runscript = "openrc-runscript"
    openscad = "openscad"
    openstep_property_list = "openstep-property-list"
    opentype_feature_file = "opentype-feature-file"
    org = "org"
    ox = "ox"
    oxygene = "oxygene"
    oz = "oz"
    p4 = "p4"
    pan = "pan"
    papyrus = "papyrus"
    parrot = "parrot"
    parrot_assembly = "parrot-assembly"
    parrot_internal_representation = "parrot-internal-representation"
    pascal = "pascal"
    pawn = "pawn"
    pep8 = "pep8"
    perl = "perl"
    php = "php"
    pic = "pic"
    pickle = "pickle"
    picolisp = "picolisp"
    piglatin = "piglatin"
    pike = "pike"
    plantuml = "plantuml"
    plpgsql = "plpgsql"
    plsql = "plsql"
    pod = "pod"
    pod_6 = "pod-6"
    pogoscript = "pogoscript"
    pony = "pony"
    postcss = "postcss"
    postscript = "postscript"
    pov_ray_sdl = "pov-ray-sdl"
    powerbuilder = "powerbuilder"
    powershell = "powershell"
    prisma = "prisma"
    processing = "processing"
    proguard = "proguard"
    prolog = "prolog"
    propeller_spin = "propeller-spin"
    protocol_buffer = "protocol-buffer"
    public_key = "public-key"
    pug = "pug"
    puppet = "puppet"
    pure_data = "pure-data"
    purebasic = "purebasic"
    purescript = "purescript"
    python_console = "python-console"
    python_traceback = "python-traceback"
    q = "q"
    q_23 = "q%23"
    qmake = "qmake"
    qml = "qml"
    qt_script = "qt-script"
    quake = "quake"
    r = "r"
    racket = "racket"
    ragel = "ragel"
    raku = "raku"
    raml = "raml"
    rascal = "rascal"
    raw_token_data = "raw-token-data"
    rdoc = "rdoc"
    readline_config = "readline-config"
    realbasic = "realbasic"
    reason = "reason"
    rebol = "rebol"
    red = "red"
    redcode = "redcode"
    regular_expression = "regular-expression"
    renpy = "ren'py"
    renderscript = "renderscript"
    rescript = "rescript"
    restructuredtext = "restructuredtext"
    rexx = "rexx"
    rich_text_format = "rich-text-format"
    ring = "ring"
    riot = "riot"
    rmarkdown = "rmarkdown"
    robotframework = "robotframework"
    roff = "roff"
    roff_manpage = "roff-manpage"
    rouge = "rouge"
    rpc = "rpc"
    rpm_spec = "rpm-spec"
    ruby = "ruby"
    runoff = "runoff"
    rust = "rust"
    sage = "sage"
    saltstack = "saltstack"
    sas = "sas"
    sass = "sass"
    scala = "scala"
    scaml = "scaml"
    scheme = "scheme"
    scilab = "scilab"
    scss = "scss"
    sed = "sed"
    self = "self"
    shaderlab = "shaderlab"
    shellsession = "shellsession"
    shen = "shen"
    sieve = "sieve"
    slash = "slash"
    _slice = "slice"
    slim = "slim"
    smali = "smali"
    smalltalk = "smalltalk"
    smarty = "smarty"
    smpl = "smpl"
    smt = "smt"
    solidity = "solidity"
    sourcepawn = "sourcepawn"
    sparql = "sparql"
    spline_font_database = "spline-font-database"
    sqf = "sqf"
    sql = "sql"
    sqlpl = "sqlpl"
    squirrel = "squirrel"
    srecode_template = "srecode-template"
    ssh_config = "ssh-config"
    stan = "stan"
    standard_ml = "standard-ml"
    starlark = "starlark"
    stata = "stata"
    ston = "ston"
    stylus = "stylus"
    subrip_text = "subrip-text"
    sugarss = "sugarss"
    supercollider = "supercollider"
    svelte = "svelte"
    svg = "svg"
    swift = "swift"
    swig = "swig"
    systemverilog = "systemverilog"
    tcl = "tcl"
    tcsh = "tcsh"
    tea = "tea"
    terra = "terra"
    tex = "tex"
    texinfo = "texinfo"
    text = "text"
    textile = "textile"
    thrift = "thrift"
    ti_program = "ti-program"
    tla = "tla"
    toml = "toml"
    tsql = "tsql"
    tsv = "tsv"
    tsx = "tsx"
    turing = "turing"
    turtle = "turtle"
    twig = "twig"
    txl = "txl"
    type_language = "type-language"
    unified_parallel_c = "unified-parallel-c"
    unity3d_asset = "unity3d-asset"
    unix_assembly = "unix-assembly"
    uno = "uno"
    unrealscript = "unrealscript"
    urweb = "urweb"
    v = "v"
    vala = "vala"
    vba = "vba"
    vbscript = "vbscript"
    vcl = "vcl"
    verilog = "verilog"
    vhdl = "vhdl"
    vim_help_file = "vim-help-file"
    vim_script = "vim-script"
    vim_snippet = "vim-snippet"
    visual_basic_net = "visual-basic-.net"
    volt = "volt"
    vue = "vue"
    wavefront_material = "wavefront-material"
    wavefront_object = "wavefront-object"
    wdl = "wdl"
    web_ontology_language = "web-ontology-language"
    webassembly = "webassembly"
    webidl = "webidl"
    webvtt = "webvtt"
    wget_config = "wget-config"
    windows_registry_entries = "windows-registry-entries"
    wisp = "wisp"
    wollok = "wollok"
    world_of_warcraft_addon_data = "world-of-warcraft-addon-data"
    x_bitmap = "x-bitmap"
    x_font_directory_index = "x-font-directory-index"
    x_pixmap = "x-pixmap"
    x10 = "x10"
    xbase = "xbase"
    xc = "xc"
    xcompose = "xcompose"
    xml = "xml"
    xml_property_list = "xml-property-list"
    xojo = "xojo"
    xpages = "xpages"
    xproc = "xproc"
    xquery = "xquery"
    xs = "xs"
    xslt = "xslt"
    xtend = "xtend"
    yacc = "yacc"
    yaml = "yaml"
    yang = "yang"
    yara = "yara"
    yasnippet = "yasnippet"
    zap = "zap"
    zeek = "zeek"
    zenscript = "zenscript"
    zephir = "zephir"
    zig = "zig"
    zil = "zil"
    zimpl = "zimpl"


