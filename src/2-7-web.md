---
title: 'Web Technologies'
geometry: margin=1in
fontsize: 12pt
colorlinks: true
---

# Basic concepts

**Resource:**  anything that might be identified by a URI.

- **Information resource:** a resource which has the property that all of its essential characteristics can be conveyed in a message.

**Representation:** data that encodes information about resource state.

**Content negotiation:** offering multiple representations for a resource and selecting the one that is the most appropriate when a representation must be served.

**Dereferencing a URI:** using a URI to access the
referenced resource.

- Forms of access includes: retrieving, adding, or modifying a representation of the resource, and deleting some or all representations of the resource.

**User agent:** one type of Web agent, a piece of software acting on behalf of a person. *For example, a web browser.*

----

## Types of standards

- **De facto standards:** arise from common usage.
  - Examples: the QWERTY keyboard layout, TeX, PDF (before 2008).
- **De jure standards:** are mandated by regulators at the local, state, federal, and/or international level.
  - Examples: International System of Units (SI), PDF (from 2008).
- **Voluntary consensus standards:** are specified within a range of private institutions, including engineering societies, trade associations, accredited standards-setting organizations, and industry consortia.
  - Examples: the Internet protocol suite (commonly known as TCP/IP), HTML, CSS.

----

## Organizations responsible for web standards

### Internet Assigned Numbers Authority (IANA)

- Coordinates the allocation of codes and numbers that form the basis for the operation of the Internet.
  - Manages the DNS root zone, and the `.int` and `.arpa` domains.
  - Coordinates the allocation of IP addresses globally.
  - Maintains registries of codes and numbers used in a variety of Internet protocols.
- IANA is performed by ICANN (Internet Corporation for Assigned Names and Numbers)

### Internet Engineering Task Force (IETF)

- An international standards organization developing Internet standards.
  - Develops TCP/IP
- Publishes Internet standards-related specifications in the RFC series of documents.

### Request for Comments (RFC)

- RFC series contains technical and organizational documents about the Internet. RFC Editor edits, publishes, and catalogs RFCs.
- Began in 1969 as a part of ARPANET project.
- Split into four streams:
  - The Internet Engineering Task Force (IETF) Stream
  - The Internet Architecture Board (IAB) Stream
  - The Internet Research Task Force (IRTF) Stream
  - The Independent Submission Stream
- Each RFC is identified by a number.
- Published RFCs never change.
- Various errors are fixed by errata.
- Amendments can be also made by writing and publishing a revised RFC.
  - An RFC can obsolete or update earlier RFCs.
- Contains two important sub-series:
  - *Best Current Practice (BCP):* documents guidelines, processes, or the operation of the IETF itseld.
  - *Internet Standard (STD)*
- BCPs and STDs are assigned a number in their subseries while retaining their RFC number. They can also be shared among several RFCs.
- **Standards Track:** the set of maturity levels of RFCs that are intended to become Internet Standards.
  - Originally, three maturity levels: Proposed, Draft and Internet.
  - Currently, Proposed and Internet Standard are used.
- **Internet-Draft:** a draft version of a specification made available for informal review and comment during the development.
  - May or may not be published as an RFC.
  - Subject to change or removal
  - Valid for maximum six months.
  - Shouldn't be cited in any formal documents, except as "work in progress"

### World Wide Web Consortium (W3C)

- The W3C is an international community where member organizations, a full-time staff, and the public work together to develop Web standards.W3C's mission is to lead the Web to its full potential.
- W3C publishes documents called Recommendations that define Web technologies and are considered Web standards.
- The director is Tim Berners-Lee, the inventor and creator of the Web.

#### W3C Design Principles

- **Web for All:** the Web must be available to all people, whatever their hardware, software, network infrastructure, native language, culture, geographical location, or physical or mental ability.
- **Web on Everything:** the Web must be accessible from a wide variety of devices.

### Web Hypertext Application Technology Working Group (WHATWG)

- A community committed to the evolution of the Web that develops standards implementable in web browsers.
- The WHATWG develops specifications called “Living Standards” that are continuously updated.

\pagebreak

# URIs

## What is a URI?

- A compact sequence of characters that identifies an abstract or physical resource.
  - A resource is not necessarily available on the Web.
  - URIs can be assigned even to objects from the real world or to concepts.
- Each URI begins with a scheme name that is separated by a ':' character from the scheme-specific part of the URI.
- Organizaiton responsible for the adminstration of the URI schemes: *IANA*

----

## URI Syntax

- Organized hierarchically. Components listed in order of decreasing significance from left to right.
- Generic syntax:
  - *schema* ':' *hier-part* ['?' *query*] ['#' *fragment*]
  - The hier-part component may consist of an authority and a path component, its syntax is:
    `'//'` authority path or path
  - When authority is present, the path must either be empty or begin with a `'/'` character.
  - When authority is not present, the path cannot begin with two `'/'` characters.
- Example:

  `https://wordery.com/search?term=scotland#results`
  - Consists of scheme, host, path, query and fragment.

### Path

- A sequence of path segments separated by a `'/'` character.
- Terminated by the first `'?'` or `'#'`, or by the end of the URI.
- The path segments `'.'` and `'..'` can be used just as in some operating systems' file directory structures.

### Query

- Indicated by the first `'?'` character and terminated by a `'#'` character or by the end of the URI.
- Contains non-hierarchical data.
- Often contains name/value pairs of the form name `'='` value delimited by an `'&'` character.

### Fragment Identifier

- Indicated by a `'#'` character and terminated by the end of the URI.
- Allows indirect identification of a secondary resource by reference to a primary resource and additional identifying information.
- The semantics of a fragment identifier are defined by the set of representations that might result from a retrieval action on the primary resource.
- The fragment identifier is separated from the rest of the URI prior to a dereference.
- URI scheme specifications must define their own syntax so that all strings matching their scheme-specific syntax must be an absolute URI without a fragment identifier.

\pagebreak

# HTTP

## What is HTTP?

- A family of stateless, application-level, request/response protocols that share a generic interface, extensible semantics, and self-descriptive messages to enable flexible interaction with network-based hypertext information systems.

### Characteristics

- **Stateless protocol:** each request message’s semantics can be understood in isolation.
- **Extensible:** HTTP defines a number of generic extension points that can be used to introduce capabilities to the protocol without introducing a new version, including methods, status codes, fields.

### Message Abstraction

Messages are intended to be self-descriptive. A message consists of the following:

#### Control Data

- Messages start with control data that describe its primary purpose.
  - Request message control data includes a request method, request target, and protocol version.
  - Response message control data includes a status code, optional reason phrase, and protocol version.
- Every HTTP message has a protocol version.

#### Header Section

- Fields that are sent or received before the content are referred to as **header fields** (or just **headers**, colloquially).
- The header section of a message consists of a sequence of header field lines.

#### Content

- Content is transferred as a stream of octets after the header section.
- It is in a format and encoding defined by the the header fields `Content-Type` and `Content-Encoding`.
- The purpose of content in a request is defined by the method semantics.
  - For example, a representation in the content of a POST request represents information to be processed by the target resource.
- In a response, the content’s purpose is defined by the request method, response status code, and response fields describing that content.
  - For example, the content of a 200 (OK) response to GET represents the current state of the target resource, as observed at the time of the message origination date.

#### Trailer Section

- Fields that are sent or received after the content are referred to as **trailer fields** (or just **trailers**, colloquially).
- Trailer fields can be used to carry checksums, digital signatures, delivery metrics, or post-processing status information.
- The trailer section of a message consists of a sequence of trailer field lines.
- Trailer fields should be processed and stored separately from header fields.

---

### HTTP methods: `GET, HEAD, POST, PUT, DELETE`

#### `GET`

- Requests transfer of a current selected representation for the target resource.
- The primary mechanism of information retrieval.
- A client can alter the semantics of GET to be a range request, requesting transfer of only some part(s) of the selected representation, by sending a `Range` header field in the request.

#### `HEAD`

- Identical to the GET method except that the server must not send content in the response.
- Can be used to obtain metadata about the selected representation without transferring its representation data.

#### `POST`

- Requests that the target resource process the representation enclosed in the request according to the resource’s own specific semantics.
- Common uses include:
  - Submitting data (e.g., form data) to a data-handling process.
  - Posting a message to a newsgroup, mailing list, or blog.
  - Creating a new resource.
  - Appending data to a resource’s existing representation(s).

#### `PUT`

- Requests that the state of the target resource be created or replaced with the state defined by the representation enclosed in the request message content.
- A successful PUT of a given representation would suggest that a subsequent GET on that same target resource will result in an equivalent representation being sent in a 200 (OK) response.

#### `DELETE`

- Requests that the origin server remove the association between the target resource and its current functionality.
- If the target resource has one or more current representations, they might or might not be destroyed by the origin server, and the associated storage might or might not be reclaimed, depending entirely on the nature of the resource and its implementation by the origin server.
- Relatively few resources allow the DELETE method.

----

### Status codes, classes of status codes

- The status code of a response is a three-digit integer code that describes the result of the request and the semantics of the response, including whether the request was successful and what content is enclosed (if any).
- All valid status codes are within the range of 100 to 599, inclusive.

#### Classes of Status Codes:

- 1*xx* (Informational): indicates an interim response for communicating connection status or request progress prior to sending a final response.
- 2*xx* (Successful): indicates that the request was successfully received, understood, and accepted.
- 3*xx* (Redirection): indicates that further action needs to be taken by the user agent in order to fulfill the request that can be performed automatically by the user agent.
- 4*xx* (Client Error): indicates that the request contains bad syntax or cannot be fulfilled.
- 5*xx* (Server Error): indicates that the server failed to fulfill an apparently valid request.

----

### Content Negotiation

- When responses convey content, whether indicating a success or an error, the origin server often has different ways of representing that information; for example, in different formats, languages, or encodings.
- Likewise, different users or user agents might have differing capabilities, characteristics, or preferences that could influence which representation, among those available, would be best to deliver.

----

### Cookies

- A name/value pair and associated metadata (attributes) sent by an origin server to a user agent using the `Set-Cookie` header field in a response.
  - An origin server can specify a scope for the cookie using the attributes.
- In subsequent requests, the user agent returns the name/value pair to the origin server in the `Cookie` header field.
- Uses:
  - Session management
  - Personalization
  - Web tracking (see the `Referer` header field)
- An origin server can send multiple cookies in a response
- When the user agent receives a `Set-Cookie` header, it stores the cookie together with its attributes.
- Subsequently, when the user agent makes an HTTP request, it includes the applicable, non-expired cookies in the `Cookie` header field.
  - It includes only the name/value pairs without the attributes!
- If the user agent receives a new cookie with the same name, `Domain` attribute, and `Path` attribute as a cookie that it has already stored, the existing cookie is replaced with the new cookie.

----

#### Third-party Cookies

- Cookies are often criticized for letting servers track users.
  - Particularly problematic are so-called thirdparty cookies.
  - In rendering an HTML document, a user agent often requests resources from other servers.
  - These third-party servers can use cookies to track the user even if the user never visits the server directly.
- Unless sent over a secure channel (such as TLS), the information in the `Cookie` and `Set-Cookie` headers is transmitted in cleartext.
  - All sensitive information conveyed in these headers is exposed to an eavesdropper and a malicious intermediary could alter it.
- Servers should encrypt and sign the contents of cookies when transmitting them to the user agent (even when sending the cookies over a secure channel).
- When using cookies over a secure channel, servers should set the `Secure` attribute for every cookie.

\pagebreak

# XML

## What is a Markup Language?

- Markup languages are computer languages for annotating text.
- They allow the association of metadata with parts of text in a clearly distinguishable way.
- Examples: AsciiDoc, Markdown, TeX, troff, Wikitext, XML

## What is XML?

- A general purpose markup language
- **In the strict sense:** A syntax for representing structured documents that enables the automatic processing of these documents.
- **In the broadest sense:** A set of related specifications that are also called collectively as **the XML family**.

### Advantages and disadvantages of XML

#### Advantages

- Simplicity
- Openness
- Vendor independence
- Platform independence
- A universal data exchange format
- Extensive infrastructure
- A **de-facto standard** in the industry

#### Disadvantages

- Verbose and cumbersome to use syntax
- Highly inefficient storage
- Complexity
  - There seems to be any number of XML-related specifications.

### Document-Centric XML

- Documents are composed of text intermingled with markups.
- Highly varied document structure.
- The ordering of elements is important.
- Such documents are primarily intended to be consumed by humans.
- For example, XHTML is such an XML format.

### Data-Centric XML

- Documents are composed of a large number of data elements.
- Less random document structure.
- The ordering of elements is less important.
- Such documents are primarily intended to be processed by computers.
- For example, SVG is such an XML format.

----

## XML Documents

- Textual objects that are well-formed according to the standard.
- Each XML document has both a logical and a physical structure.
  - Physically, a document is composed of storage units called entities.
  - Logically, a document is composed of declarations, elements, comments, processing instructions, and other structural components.

----

## Elements

- Each element is delimited by a start-tag and an end-tag, or is is made up from a single empty-element tag.

```XML
<author>Sir Arthur Conan Doyle</author>
<message xml:lang="en">Hello, World!</message>
<img src="logo.png" alt="Logo"/>
```

----

## Well-Formedness

- A single top-level element called the **root element** contains all the other elements.
- Each start-tag has a corresponding end-tag.
- Elements are properly nested and and do not overlap.
- Each entity referenced in the document is well-formed.
- Many other constrains, the so-called **well-formedness constraints**, must be fulfilled.

----

## Markup constructs

### Start-tag, end-tag, and empty-element tag

- **Start-tag**
  - `<title>, <title xml:lang="en">`{.xml}

- **End-tag**
  - `</title>`{.xml}

- **Empty element tag**
  - `<br/>, <hr />, <img src="logo.png" alt="Logo"/>`{.xml}

- **Well-formedness constraint**: an attribute name must not appear more than once in the same start-tag or empty-element tag.
- The order of attribute specifications in a start-tag or empty-element tag is not significant.

### Character reference

- In text, attribute values, and literal entity values Unicode characters may also be expressed using character references of the form:
  - `&#nnnn;` where *nnnn* is a sequence of decimal digits
  - `&#xhhhh;` where *hhhh* is a sequence of hexadecimal digits

### Entity reference

- An entity reference refers to the content of a named entity: `&name;`
- Parameter-entity reference: `%name;`

### Comment

- They may appear anywhere in a document outside other markup.
  - `<!-- This is a comment -->`{.xml}

### Processing instruction

- They contain instructions for applications.
  - `<?xml-stylesheet type="text/css" href="style.css"?>`{.xml}

### CDATA section delimiters

- They may occur anywhere where character data may occur.
  - used to escape blocks of text containing characters which would otherwise be recognized as markup.
  - Within a CDATA section, only the ']]>' string is recognized as markup.
  - `<![CDATA[if (0 < n && n <= 10)]]>`{.xml}

### XML declaration

- XML documents should begin with an XML declaration which specifies the version of XML being used.
  - The character encoding must be specified if the encoding used is not UTF-8 or UTF-16, unless an encoding is determined by a higher-level protocol (e.g., HTTP).
  - `<?xml version='1.0' encoding='UTF-8'?>`{.xml}

### Document type declaration

- It contains and/or points to markup declarations that provide a grammar for a class of documents.
  - This grammar is known as a document type definition, or DTD.
- The name in the document type declaration specifies the element type of the root element
- Document type declarations that point to an external entity containing markup declarations called the external DTD subset:
  - `<!DOCTYPE score-partwise SYSTEM "http://www.musicxml.org/dtds/partwise.dtd">`{.xml}
- A document type declaration that contains markup declarations called the internal DTD subset:

```XML
<!DOCTYPE message [
    <!ELEMENT message (#PCDATA)>
    <!ATTLIST message
        xml:lang CDATA #IMPLIED>
]>
```

- A document type declaration that points to an external DTD subset and also contains an internal DTD subset:

```XML
<!DOCTYPE play SYSTEM "play.dtd" [
    <!ENTITY r "Rosencrantz">
    <!ENTITY g "Guildenstern">
    <!ENTITY rag "&r; and &g;">
]>
```

----

\pagebreak

# HTML

## What is HTML?

- *"HTML is the World Wide Web's core markup language."*
- "“"[...] a semantic-level markup language and associated semantic-level scripting APIs for authoring accessible pages on the Web ranging from static documents to dynamic applications."
- Originally, the HTML5 specification was developed by the WHATWG.

----

## The elements of HTML

- Elements, attributes, and attribute values in HTML are defined to have certain meanings (semantics).
  - For example, the `ol` element represents an ordered list, and the `lang` attribute represents the language of the content.
- Authors must not use elements, attributes, or attribute values for purposes other than their appropriate intended semantic purpose.
- The majority of presentational features from previous versions of HTML are no longer allowed.
- The problems of presentational markup:
  - Poorer accessibility.
  - Higher cost of maintenance.
  - Larger document sizes.
- The only remaining presentational markup features in `HTML` are the `style` attribute and the `style` element.

----

## HTML Syntaxes

- HTML defines an abstract language for describing documents and two concrete syntaxes that can be used to transmit resources that use this abstract language.

### HTML Syntax

- While it bears a close resemblance to `SGML` and `XML`, it is a separate language with its own parsing rules.
- It is compatible with most legacy web browsers.
- File extension: `.html`, `.htm`
- Media type: `text/html`

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Sample Page</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <p>Hello, World!</p>
    </body>
</html>
```

- A document type declaration is required.
- Special characters:
  - Element text must not contain the '`<`' character or an ambiguous ampersand.
  - Attribute values must not contain an ambiguous ampersand.
- Ambiguous ampersand ('`&`'):
  - An '`&`' character that is followed by one or more ASCII alphanumerics, followed by a '`;`', where these characters do not match any of the named character references defined by the standard. (e.g., `&nosuchchar;`).
- Element and attribute names are case-insensitive.
  - Element and attribute names, even those for foreign elements, may be written with any mix of lower- and uppercase letters that are an ASCII case-insensitive match for the name of the element/attribute.
  - There must never be two or more attributes on the same start tag whose names are an ASCII caseinsensitive match for each other.
- Unquoted attribute value syntax:
  - If an attribute value other than the empty string does not contain any literal whitespace character it can be specified omitting the attribute value delimiters.
  - The following are equivalent:

```HTML
<input value="yes">
<input value=yes>
```

- Boolean attributes:
  - A number of attributes are boolean attributes.
  - The presence of a boolean attribute on an element represents the true value, and the absence of the attribute represents the false value.
  - If the attribute is present, its value must either be the empty string or a value that is a case-insensitive match for the attribute’s canonical name, with no leading or trailing white space.
- Void elements:
  - Only have a start tag, end tags must not be specified for them.
  - Examples: `br`, `img`, `input`, `link`, `meta`, ...
- Foreign elements must either have a start tag and an end tag, or a start tag that is marked as self-closing, in which case they must not have an end tag.
- Optional tags:
  - The start and end tags of certain elements can be omitted.
  - For example, an HTML document always has a root html element, even if the string `<html>` doesn't appear anywhere in the markup.
  - An `li` element's end tag may be omitted if it is immediately followed by another `li` element or if there is no more content in the parent element.
  - An `html` element's start tag may be omitted if the first thing inside the element is not a comment.
  - An `html` element's end tag may be omitted if the element is not immediately followed by a comment.

----

## The HTML Document Type Declaration

- In the HTML syntax the document type declaration `<!DOCTYPE html>` is required, whose only purpose is to to ensure that the document is rendered in standards mode.

----

## Document Object Model (DOM)

- A DOM tree is an in-memory representation of a document.
- DOM is an API for accessing and manipulating documents (in particular, HTML and XML documents).
- Each such document is represented as a tree that consists of the following kinds of nodes:
  - `Document, DocumentType, DocumentFragment, Element, Text, ProcessingInstruction` and `Comment`.
- Each node is represented by an object with an API so that they can be manipulated.
- Web IDL is an interface definition language that can be used to describe interfaces that are intended to be implemented in web browsers.
- The HTML specification defines additional interfaces that extend DOM interfaces for representing HTML elements.
- The DOM is not just an API, the conformance criteria of HTML implementations are defined in terms of operations on the DOM.
- The specifications are mostly phrased in terms of DOM trees, instead of markup.
- A DOM tree can be manipulated from scripts in the page.

\pagebreak

# CSS

## What is CSS?

- A style sheet language for describing the rendering of structured documents (such as HTML and XML).
  - Supports rendering on different devices, such as screens, printers, and Braille devices.
- Separates the presentation style of documents from the content of documents.

### Development

- Developed by the CSS Working Group of W3C.

### Levels

- CSS does not have versions in the traditional sense, instead it has levels
- Each level of CSS builds on the previous, refining definitions and adding features.

----

## The CSS box model

- CSS takes a source document, organized as a tree, and renders it onto a canvas (such as the screen) generating an intermediary structure, the **box tree**, which represents the formatting structure of the rendered document.
- Each box in the box tree represents a corresponding element (or pseudo-element) from the document in space and/or time on the canvas.
- For each element, CSS generates zero or more boxes as specified by that element’s `display` property.
  - Typically, an element generates a single box.

![Box Model](imgs/boxmodel.png)

----

## Syntactic Elements

### Characters

- CSS uses the Unicode character set.

### Escape Sequences

- Unicode characters can be specified with escape sequences of the form \ *hhhhhh*, where *hhhhhh* is a sequence of one to six hexadecimal digits representing the code point of the Unicode character.
- Special characters can be escaped with the a '\' character.

### Comments

- Comments can be placed between the `/*` and `*/` delimiters.
- Can occur anywhere but in tokens.
- Cannot be nested.

### Declaration Blocks

- Start with a '`{`' character and end with a '`}`' character, in between there must be a list of zero or more declarations.
  - Declarations are of the form *name:value*, where whitespace characters are allowed before and after tokens.
  - Declarations must end with a '`;`' character.

### Rule Sets (Style Rules)

- Consist of a selector (or a list of selectors separated with a '`,`' character) followed by a declaration block.

### At-rules

- Define special processing rules or values.
- Start with a '`@`' character, followed by an identifier and includes everything up to the next '`;`' character, or the next declaration block.

----

## Properties

- Parameters defined by CSS for controlling the rendering of documents.
- Properties have names and values.
- **Shorthand property**: A property that allows authors to specify the values of several properties simultaneously.
  - Example, `margin` property is a shorthand for `margin-top`, `margin-right`, `margin-bottom`, and `margin-left`

----

## Selectors

- Selectors express pattern matching rules that determine which style rules apply to elements.
- Selectors are case-insensitive within the ASCII range.

### Type Selector

- Written as a CSS qualified name, generally, an identifier.
- Matches the elements of that name.

```css
p { color: red }
a { text-decoration: none}
```

### Universal Selector

- Written as `*`.
- It matches all elements.
- May be omitted from a simple selector, if it is not the only component.

### Attribute Selectors

- In each attribute selector, *val* must be a CSS identifier or a string.

- [att]
  - Matches elements with the *att* attribute.
- [att=val]
  - Matches elements with the *att* attribute whose value is exactly *val*.

```css
style[type=italic] {
    font-style: italic;
}
```

### Class Selector

- *.val* selector

```css
div.centered {
    margin-left: auto;
    margin-right: auto;
}
```

### ID Selector

- A selector of the form *#identifier* matches the element with that identifier.
- The identifier must be provided by an attribute of type ID in the document.

```css
#footer { text-align: center }
```

### Pseudo-classes

- Selectors of the form :*identifier* or :*identifier*(*value*).
  - Case-insensitive names
- Permit selection based on information that lies outside of the document or that cannot be expressed using the other simple selectors.
- Some pseudo-classes are mutually exclusive.

#### Dynamic Pseudo-classes

- An element may acquire or lose a dynamic pseudo-class while a user interacts with the document.
- **Link pseudo-classes:**
  - `:link`: applies to links that have not yet been visited.
  - `:visited`: applies to links that have been visited by the user.
- **User action pseudo-classes:**
  - `:hover`: applies while the user designates an element with a pointing device, but does not necessarily activate it.
  - `:active`: applies while an element is being activated by the user.
  - `:focus`: applies while an element has the focus (accepts keyboard or mouse events, or other forms of input).

```css
:link {
    border-width: medium;
    border-style: solid;
    text-decoration: none;
}
:visited {
    text-decoration: line-through
}
a:hover {
    text-decoration: overline underline;
    color: red;
}
a:active { font-weight: bolder }
```

#### The `:lang(C)` Pseudo-class

- Represents elements that are in language *C*.
  - *C* is a CSS identifier (language code).
  - Example: `:lang(en)`, `:lang(en-GB)`, `:lang(en-US)`

```css
q:lang(hu) {
    quotes: "„" "”" "»" "«";
}
```

#### Structural Pseudo-classes

- Only elements are counted when calculating the position of an element in its list of siblings.
- Index numbering starts at 1.
- **`:root`**: represents the root element of the document.
- **`:only-child`**: represents elements that have no siblings.
- **`:only-of-type`**: represents elements that have no siblings with the same element name.
- **`:empty`**: represents elements that have no children at all.
- `:nth-child()`, `:nth-last-child()`, `:nth-of-type()` and `:nth-last-of-type()`:
  - The argument *a*n+0 can be specified as *a*n in short.
  - The argument 0n+*b* can be specified as *b* in short.
  - For a negative *b* the argument must be specified as *a*n-*b*, the form *a*n+-*b* is invalid.
  - The argument 2n can be specified as even, the argument 2n+1 as odd, respectively.

### Pseudo-elements

- Pseudo-elements allow authors to refer to content in the document that is otherwise inaccessible.
- Only one pseudo-element may appear per selector.
- CSS3 uses '`::`' for pseudo-elements to distinguish them from pseudo-classes.
  - For compatiblity '`:`' can be used also.
- `::first-line`: represents the first formatted line of an element.
- `::first-letter`: represents the first letter or digit of an element, if it is not preceded by any other content (such as images) on its line.
- `::before` and `::after`: can be used to describe generated content before or after an element’s content.

----

## Combinators

### Descendant combinator

- Whitespace that separates two sequences of simple selectors.
- `thead th { background-color: darkgrey }`{.css}

### Child combinator

- A '>' character that separates two sequences of simple selectors
- `nav > div { display: inline }`{.css}

### Next-sibling combinator

- A '+' character that separates two sequences of simple selectors.
- `h1 + p { text-indent: 0 }`{.css}

\pagebreak

# JSON

## What is JSON?

- Lightweight, textual, and platform independent data exchange format.
- Used for representing structured data.
- Can be read and written easily by humans.
- Can be generated and processed easily by computer programs.
- Originates from the ECMAScript programming language.

## Comparison of JSON and ECMAScript

- Starting with ECMAScript 2019, JSON is a syntactic subset of ECMAScript.

## Comparison of JSON and XML

- JSON can be used as an alternative to XML for data exchange.
- Provides the same advantages as XML but without its disadvantages.
- The main difference is that JSON is dataoriented, while XML is document-oriented.
  - JSON is the perfect choice for representing data structures.

### XML:

```xml
<movie>
    <title>The Dark Knight</title>
    <year>2008</year>
    <url>https://www.imdb.com/title/tt0468569/</url>
    <standalone>false</standalone>
</movie>
```

### JSON:

```json
{
    "movie": {
        "title": "The Dark Knight",
        "year": 2008,
        "url": "https://www.imdb.com/title/tt0468569/",
        "standalone": false
    }
}
```

### Common characteristics of JSON and XML:

- Simplicity (undoubtedly JSON is the winner)
- Can be read and written easily by humans
- Can be generated and processed easily by computer programs (undoubtedly JSON is the winner)
- Interoperability
- Open standard
- Self-describing data representation
- Universal data exchange format

----

## Primitive types

### Strings

- Sequences of Unicode characters delimited by quotation marks (U+0022).

### Numbers

- No constraints are imposed on the range and precision of numbers.
- Implementations should consider interoperability.
  - For example, they should use double-precision numbers.

### Booleans

### `null`

----

## Structured types

### Arrays

- Ordered sequences of zero or more values (can be empty).
- Elements can be of any type (including arrays).
- `["Athos", "Porthos", "Aramis", "d'Artagnan"]`{.json}

### Objects

- Unordered collections of zero or more name/value pairs.
- A name is a string, a value is a JSON value.
- Name/value pairs are also called as members.

```json
{
    "title": "Alien",
    "year": 1979,
    "rating": 8.5,
    "votes": 643196,
    "genres": ["horror", "sci-fi"],
    "url": "http://www.imdb.com/title/tt0078748/"
}
```