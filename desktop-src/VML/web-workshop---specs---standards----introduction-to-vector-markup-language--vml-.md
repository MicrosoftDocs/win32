---
title: Vector Markup Language (VML)
description: Vector Markup Language (VML)
ms.assetid: 1f30d60f-3d4f-43e4-9a2b-424a5ee8f852
keywords:
- Vector Markup Language (VML),about
- VML (Vector Markup Language),about
- vector graphics,about
- vector graphics,Vector Markup Language (VML)
- Vector Markup Language (VML),World Wide Web Consortium (W3C)
- VML (Vector Markup Language),World Wide Web Consortium (W3C)
- vector graphics,World Wide Web Consortium (W3C)
- vector graphics,VML benefits
- Vector Markup Language (VML),benefits
- VML (Vector Markup Language),benefits
ms.topic: article
ms.date: 05/31/2018
---

# Vector Markup Language (VML)

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!NOTE]
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

Vector Markup Language (VML) is an XML-based exchange, editing, and delivery format for high-quality vector graphics on the Web that meets the needs of both productivity users and graphic design professionals. XML is an emerging simple, flexible, and open text-based language that complements HTML. (See the [XML section](/docs/?frame=true) of the MSDN Library for detailed information on XML.)

VML is currently supported by Microsoft Internet Explorer version 5.0 or later.

VML has been proposed to the W3C as a standard for vector graphics on the Web (see [Vector Markup Language (VML)](https://www.w3.org/TR/NOTE-VML)). Microsoft is continuing to lead the charge in the development and implementation of XML-based technologies, working with leading industry partners (AutoDesk, Hewlett-Packard, Macromedia, Visio) and the W3C to advance Web-based standards. We expect to work with the W3C to ultimately drive to one standard format for vector graphics on the Web.

VML is also supported by Microsoft Office 2000 or later. Microsoft Word, Microsoft Excel, and Microsoft PowerPoint can be used to create VML graphics.

### Using VML

To use VML in your web pages, use a style element to import the VML behavior, as shown in the following code.

```
<style>v\: * { behavior:url(#default#VML); display:inline-block }</style>
```

Next, declare the VML namespace, as shown in the following code sample.

```
<xml:namespace ns="urn:schemas-microsoft-com:vml" prefix="v" />
```

Finally, add VML elements to define visuals effects. For example, the following VML code creates a red oval.

```
<v:oval style="width:100pt;height:50pt" fillcolor="red">
</v:oval>
```

> [!NOTE]
> For best results when using strict mode documents, be sure that your markup is valid and well-formed. For more information, please see the !DOCTYPE reference page.


### Benefits of VML

-   VML makes authoring easier for productivity users and authors. It facilitates the exchange (via cut and paste) and subsequent editing of vector graphics between a wide variety of productivity and design applications.
-   VML provides faster graphic downloads and a better user experience. It allows the delivery of high-quality, fully integrated, scalable vector graphics to the Web, in an open text-based format. Rather than referencing graphics as external files, VML graphics are delivered inline with the HTML page, allowing them to interact and scale with user interaction.
-   VML is open and standards-based. It is an XML-based format. XML 1.0 is an open, simple, text-based language for describing structured data on the Web, and complements HTML for display. VML also supports other W3C standards, such as Cascading Style Sheets 2.0 (CSS), which specifies style information and 2-D positioning, as well as the Document Object Model (DOM), which allows developers to interact consistently with page elements as objects.

### For additional information

See the links below:

-   For answers to frequently asked questions about VML, see the [VML FAQ](frequently-asked-questions-about-vml.yml).
-   For a tutorial on using VML on Web pages, see [How to Use VML on Web Pages](web-workshop---specs---standards----how-to-use-vml-on-web-pages.md), which complements the [VML specification](https://www.w3.org/TR/NOTE-datetime.html) submitted to the W3C.
-   For information on VML data types, see the [Basic VML Types](basic-vml-types.md) document.
-   For the complete reference on VML, including information on how to use VML with tags as well as scripting, see the [VML Reference](msdn-online-vml-introduction.md).
