---
title: Embedding COM Objects in Web Pages
description: You can use COM objects in webpages. To do this, first create an instance of that COM object. After an object instance is created, you can use it in subsequent scripts on that webpage.
ms.assetid: 7e2c9da7-aeae-4206-8be9-1303240b2b1d
ms.topic: article
ms.date: 05/31/2018
---

# Embedding COM Objects in Web Pages

You can use COM objects in webpages. To do this, first create an instance of that COM object. After an object instance is created, you can use it in subsequent scripts on that webpage.

To create a COM object instance in a webpage, you can use an OBJECT tag. Alternatively, if your scripting language provides a native way to create COM objects, you can create an object instance using script.

Note that embedding COM objects in webpages only works with browsers that support ActiveX and COM, for example Internet Explorer.

The following example illustrates using the OBJECT tag to embed a COM object in a webpage:

``` syntax
<OBJECT 
  ID = vid 
  CLASSID = "clsid:31263EC0-2957-11CF-A1E5-00AA9EC79700" 
  BORDER = 0 
  VSPACE = 0 
  HSPACE = 0 
  ALIGN = TOP 
  HEIGHT = 100% 
  WIDTH = 100%
>
</OBJECT>
 
```

You can also create a COM object instance in script, if your scripting language provides a way to create COM objects. For example, VBScript provides the CreateObject method and JScript provides the ActiveXObject object. Creating objects in script is illustrated in the following examples.

``` syntax
<SCRIPT LANGUAGE = "VBScript">
  Dim objXL
  Set objXL = CreateObject("Excel.Application")
</SCRIPT>
 
<SCRIPT LANGUAGE = "JScript">
  var objXL = new ActiveXObject("Excel.Application");
</SCRIPT>
 
```

In addition to the CreateObject method and the ActiveXObject object, both VBScript and JScript provide the method GetObject, which returns an object instance.

After a COM object has been created, you can reference it in subsequent scripts by using the identifier specified in the OBJECT tag's ID attribute. In the preceding example, this identifier was specified as "vid." Note that the script that uses the COM object must appear after the OBJECT tag or script that creates the object instance; otherwise, the object identifier is undefined. The following script uses the objXL object to display the version information for Microsoft Excel.

``` syntax
<SCRIPT LANGUAGE = "VBScript">
  Msgbox objXL.Version
</SCRIPT>
 
```

If you are writing scripts embedded in a webpage, the browser also exposes an object model that your scripts can access. The model used by Internet Explorer conforms to the Document Object Model (DOM) proposed by the World Wide Web Consortium (W3C).

## Related topics

<dl> <dt>

[Scripting with COM Objects](scripting-with-com-objects.md)
</dt> </dl>

 

 




