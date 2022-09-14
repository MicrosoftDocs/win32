---
title: Using COM Objects in Active Server Pages
description: You can script COM objects in Active Server Pages (ASP) applications.
ms.assetid: 3a074360-8b6c-4cb6-813b-73863fe11c46
ms.topic: article
ms.date: 05/31/2018
---

# Using COM Objects in Active Server Pages

You can script COM objects in Active Server Pages (ASP) applications. To do so, you must first create an instance of the object either by using the OBJECT tag or by calling the CreateObject method of the ASP Server object. Once a COM object has been created, you can use it in subsequent scripts on the ASP page.

Using ASP, you can work with many different types of scripting engines, each of which supports a different scripting language. ASP comes with VBScript and JScript scripting engines. You can also plug in scripting engines developed by other companies to support languages such as PerlScript, PScript, Python, and others.

If you do not set the scripting language for an ASP page, VBScript is the default. To specify a scripting language other than VBScript, include a line such as the following at the top of each ASP page:

``` syntax
<%@ LANGUAGE=JScript %>
 
```

To use a COM object in an ASP page, you must first create an instance of that object. You do this by using the OBJECT tag and specifying the value "SERVER" for the RUNAT attribute, as shown in the following example. By default, the OBJECT tag creates an instance of the object on the client. Setting the RUNAT attribute to SERVER causes the object to be created on the server. The object must run on the server in order to be used by ASP.

``` syntax
<OBJECT 
RUNAT=SERVER 
ID=MyAds 
CLASSID="Clsid:1621F7C0-60AC-11CF-9427-444553540000">
</OBJECT> 
 
```

You can also create an instance of a COM object on an ASP page by calling the CreateObject method of the ASP Server object. Using Server.CreateObject is slower than creating the object using an OBJECT tag, but it is slightly more readable because it specifies the programmatic identifier instead of the class identifier of the COM object. The Server object is exposed by ASP and does not need to be created. How to call Server.CreateObject is illustrated in the following examples. The first example is VBScript:

``` syntax
<% 
  Set MyAds = Server.CreateObject("MSWC.AdRotator") 
%>
 
```

The next example is JScript:

``` syntax
<% 
  var MyAds = Server.CreateObject("MSWC.AdRotator") 
%>
 
```

Calling CreateObject is slower than using the OBJECT tag to create a COM object. In applications where performance is critical, you should use the OBJECT tag.

After you have created an instance of the COM object, you can use it in scripts. Doing this is illustrated in the VBScript example following, which sets the value of the COM object's Border property.

``` syntax
<% MyAds.Border = 0 %>
 
```

## Related topics

<dl> <dt>

[Scripting with COM Objects](scripting-with-com-objects.md)
</dt> </dl>

 

 




