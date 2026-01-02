from flask import Flask, render_template, request

TAGS = ['a','a2','abbr','acronym','address','animate','animatemotion','animatetransform','applet','area','article','aside','audio','audio2','b','bdi','bdo','big','blink','blockquote','body','br','button','canvas','caption','center','cite','code','col','colgroup','command','content','custom tags','data','datalist','dd','del','details','dfn','dialog','dir','div','dl','dt','element','em','embed','fieldset','figcaption','figure','font','footer','form','frame','frameset','h1','head','header','hgroup','hr','html','i','iframe','iframe2','image','image2','image3','img','img2','input','input2','input3','input4','ins','kbd','keygen','label','legend','li','link','listing','main','map','mark','marquee','menu','menuitem','meta','meter','multicol','nextid','nobr','noembed','noframes','noscript','object','ol','optgroup','option','output','p','param','picture','plaintext','pre','progress','q','rb','rp','rt','rtc','ruby','s','samp','script','section','select','set','shadow','slot','small','source','spacer','span','strike','strong','style','sub','summary','sup','svg','table','tbody','td','template','textarea','tfoot','th','thead','time','title','tr','track','tt','u','ul','var','video','video2','wbr','xmp','xss']

EVENTS = ['onafterprint','onafterscriptexecute','onanimationcancel','onanimationend','onanimationiteration','onanimationstart','onauxclick','onbeforecopy','onbeforecut','onbeforeinput','onbeforeprint','onbeforescriptexecute','onbeforeunload','onbegin','onblur','oncanplay','oncanplaythrough','onchange','onclick','onclose','oncontextmenu','oncopy','oncut','ondblclick','ondrag','ondragend','ondragenter','ondragexit','ondragleave','ondragover','ondragstart','ondrop','ondurationchange','onend','onended','onerror','onfocusin','onfocusout','onformdata','onfullscreenchange','onhashchange','oninput','oninvalid','onkeydown','onkeypress','onkeyup','onload','onloadeddata','onloadedmetadata','onloadstart','onmessage','onmousedown','onmouseenter','onmouseleave','onmousemove','onmouseout','onmouseover','onmouseup','onmozfullscreenchange','onpagehide','onpageshow','onpaste','onpause','onplay','onplaying','onpointercancel','onpointerdown','onpointerenter','onpointerleave','onpointermove','onpointerout','onpointerover','onpointerup','onpopstate','onprogress','onratechange','onrepeat','onreset','onresize','onscroll','onscrollend','onseeked','onseeking','onselect','onshow','onsubmit','onsuspend','ontimeupdate','ontoggle','ontouchend','ontouchmove','ontouchstart','ontransitioncancel','ontransitionrun','onunhandledrejection','onunload','onvolumechange','onwebkitanimationiteration','onwheel']

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    name = request.args.get('name', None)
    if not name:
        return render_template('home.html')

    error = check_name(name.lower())
    if error:
        return error, 418
    
    return render_template('name.html', name=name)

def check_name(name):
    for tag in TAGS:
        if f'<{tag} ' in name:
            return f'Tag {tag} is not allowed'
    
    for event in EVENTS:
        if f' {event}=' in name:
            return f'Event {event} is not allowed'
        
    return None