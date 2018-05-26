---
title: Reading the Schema
description: Most providers support the schema that is shipped with Active Directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: cc35789e-5cfe-49e9-9fb3-489b949768c5
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Reading the Schema

Most providers support the schema that is shipped with Active Directory. The schema contains class and attribute definitions. ADSI abstracts the schema in "Provider://schema". Each object carries the schema location in which its class is defined. You can use the [**IADs::get\_Class**](iads-property-methods.md) property method to obtain this information.

To bind to the schema container on a particular domain, do the following:


```VB
Dim SchemaContainer As Object
Set SchemaContainer = GetObject("LDAP://Fabrikam/Schema")
```

<span codelanguage="ManagedCPlusPlus"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>hr = ADsGetObject(L&quot;LDAP://Fabrikam/Schema&quot;, IID_IADsContainer, (void**) &amp;pSchema );</code></pre></td>
</tr>
</tbody>
</table>



To list information in the schema container, bind to the container and enumerate each object in the container as shown in the following:


```VB
Dim prop As Object
Dim obj As Object
Dim SchemaContainer As Object
Dim Class As Object

Set SchemaContainer = GetObject("LDAP://Fabrikam/Schema")
'Show all items in the schema container
For Each obj In SchemaContainer
     Debug.Print obj.Name & " (" & obj.Class & ")"
Next

'Show the optional attributes
For Each prop In Class.OptionalProperties
   Debug.Print prop
Next
```

<span codelanguage="ManagedCPlusPlus"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>IADsContainer *pSchema=NULL;
 HRESULT hr;

 CoInitialize(NULL);

 hr = ADsGetObject(L&quot;LDAP://Fabrikam/Schema&quot;, 
                   IID_IADsContainer, (void**) &amp;pSchema );

 if ( !SUCCEEDED(hr) )
 {
   return hr;
 }

 // Enumerate schema objects
 IEnumVARIANT *pEnum = NULL;
 hr = ADsBuildEnumerator( pSchema, &amp;pEnum );
 pSchema-&gt;Release(); // This is no longer needed, since we have the enumerator already.
    
 if ( SUCCEEDED(hr) )
 {
   VARIANT var;
   ULONG lFetch;
   IADs *pChild=NULL;
   VariantInit(&amp;var);
        
   while( SUCCEEDED(ADsEnumerateNext( pEnum, 1, &amp;var, &amp;lFetch )) &amp;&amp; lFetch == 1 )
   {
     hr = V_DISPATCH(&amp;var)-&gt;QueryInterface( IID_IADs, (void**) &amp;pChild );
     if ( SUCCEEDED(hr) )
     {
       BSTR bstrName;
       BSTR bstrClass;
       // Get more information on the child classes
       pChild-&gt;get_Name(&amp;bstrName);
       pChild-&gt;get_Class(&amp;bstrClass);
                
       printf(&quot;%S\t\t(%S)\n&quot;, bstrName, bstrClass );
                
       // Clean-up
       SysFreeString(bstrName);
       SysFreeString(bstrClass);
                
       pChild-&gt;Release();
     }
     VariantClear(&amp;var);
   }
 }

 CoUninitialize();</code></pre></td>
</tr>
</tbody>
</table>



You can also bind to an object and get the schema location, as shown in the following:


```VB
Dim prop As Object
Dim dom As Object
Dim Class As Object

Set dom = GetObject("LDAP://Fabrikam")
Debug.Print dom.Schema
Set Class = GetObject(dom.Schema)
'Mandatory attributes
For Each prop In Class.MandatoryProperties
    Debug.Print prop
Next
```



 

 




