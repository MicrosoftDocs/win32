---
title: Benefits of Using ADSI Extensions
description: The way in which extension methods are implemented depends on the extension writer.
ms.assetid: dbd1a203-b94c-4739-8c9d-aed1c9b43426
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Benefits of Using ADSI Extensions

The way in which extension methods are implemented depends on the extension writer. An extension writer may even implement a method completely outside the scope of the directory. For example, a developer of backup and restore software plans to extend an object called **computer**. The developer must create two methods: **BackUp** and **Restore**. These methods operate remotely on the physical computer that the **computer** object in the directory points to. By acting as an extension, the component accesses the ADSI infrastructure and is viewed by ADSI clients as an integral part of the object.

The following scenarios describe situations where creating an extension to ADSI would be advantageous:

-   Create an extension to integrate a component with the directory object. Because there is a **user** object in the directory, an HR developer may wish to create an ADSI extension that populates other data in the directory when a **user** is created.
-   Create an extension if a component requires a directory lookup. A component may require a directory as a starting point for a lookup. For example, when creating a new application. An application object, **ToolApp**, can be published in the directory. Your application may support status notifications on a collection of mail servers. You decide to make this application an ADSI extension.

    Now, a user may search for all instances of **ToolApp** in the directory. For each object returned, the user may issue a call to **NotifyNow()**. An application or extension can obtain more current object data in the directory and notify each server asynchronously.

-   Create an extension as a junction between namespaces and programming models. For example, an ISV invents a new object model for print services. The **printQueue** object is already defined in the directory. The ISV can create an ADSI extension and associate it with the **printQueue** object. ADSI users can bind to a **printQueue** object and start using the object model for the ISV. From the ADSI client perspective, this junction point is transparent.
-   Create an extension to simplify tasks. Many tasks in the directory can be accomplished by searching and setting multiple attributes in an object or multiple objects. By creating a single function to manipulate multiple attributes, it simplifies development for application and script writers.

For ADSI clients, extensions enrich the ADSI programming environment in several ways:

-   Developers creating ADSI clients do not have to learn a new programming model. The extensions are part of ADSI. They would use the same paradigm for searching, data manipulation, and securing objects.
-   Administrators can manage related directory-enabled applications using extensions.
-   Extension consumers can view an ADSI object and extension as one integrated object.
-   Existing components may be integrated with ADSI, which enables extensions to leverage existing investments and create synergy between components.

ADSI extensions were designed with the following objectives:

-   Easy to implement. With the current existing Microsoft technologies, Microsoft Visual C++ development system, and the Active Template Library, an extension can be created quickly.
-   Clients view one IDispatch. From the perspective of script and Automation writers, the extension methods and properties are transparently blended into one ADSI object.
-   Independent. Extension writers can independently extend ADSI without prior knowledge of existing extensions.

Consider this scenario: A corporate developer or an ISV needs to develop a backup program. This backup application enables an administrator to back up all computers in an organizational unit. With an ADSI extension, the following script is possible.


```VB
Dim ou
On Error Resume Next
Set ou = GetObject("LDAP://OU=Sales, DC=Fabrikam, DC=COM")
If Err.Number<>0 Then
    MsgBox("An error has occurred.")
    Err.Clear
    Set ou = Nothing
    Exit Sub
End If

ou.Filter = Array("computer")

For each comp in ou
   Debug.Print comp.Get("networkAddress")
   Debug.Print comp.LastBackUp
   comp.BackUpNow
Next
```



**LastBackUp** is a property and **BackUpNow** is a method that the extension writer provides. The code shows the benefits for both extension consumers and providers. The extension writer does not have to create a new way of filtering, searching, and accessing the directory. The extension consumer does not have to relearn a new programming paradigm. New methods and properties that the extension writer provides are viewed as part of ADSI.

 

 




