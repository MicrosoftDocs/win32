---
title: Early Binding Support
description: The following code example presents a scenario with early binding support in place.
ms.assetid: 3ca955cc-a9cd-4309-8617-89fe50b65c3d
ms.tgt_platform: multiple
keywords:
- extensions ADSI , early binding support
- binding AD , early binding support
ms.topic: article
ms.date: 05/31/2018
---

# Early Binding Support

The following code example presents a scenario with early binding support in place.


```VB
Dim x as IADsUser
Dim y as IADsExt1
Dim z as IADsExt2
 
Set x = GetObject("LDAP://CN=JeffSmith, OU=Sales, 
                   DC=Fabrikam,DC=COM")
x.SetPassword("newPassword")
 
Set y = x
y.MyNewMethod( "\\srv\public")
y.MyProperty = "Hello World"
 
Set z = y
z.OtherMethod()
z.OtherProperty = 4362
 
Debug.Print x.LastName
 
Set z = GetObject("LDAP://CN=Jeff,OU=Engr, 
                   DC=Fabrikam,DC=COM")
z.OtherProperty = 5323
```



In this code example, two extension components extend a **user** object. Each extension publishes its own interface. Each extension does not recognize the other extension interface; only ADSI recognizes the existence of both extensions. Each extension delegates its [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) to ADSI. ADSI acts as an aggregator for both extensions, and any other future extensions. Querying an interface from any extension, or from ADSI, yields the same consistent result.

The following procedure describes how to create an extension.

## Step 1: Add Aggregation to Your Component

Follow the COM specification for adding aggregation to your component. In summary, you must accept the *pUnknown* requests to your component during **CreateInstance**, and delegate the *pUnknown* to the aggregator's [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) if the component is aggregated.

## Step 2: Register Your Extension

Now you must decide which directory class to extend. You cannot use the same interfaces to accomplish this that you would use for an ADSI interface, for example, [**IADsUser**](/windows/desktop/api/Iads/nn-iads-iadsuser), [**IADsComputer**](/windows/desktop/api/Iads/nn-iads-iadscomputer). Directory objects are persisted in the directory, while your extension and ADSI are running on the client computer. Directory object examples are **user**, **computer**, **printQueue**, **serviceConnectionPoint**, and **nTDSService**. You can add a new class in Active Directory and create a new extension for this new class as well.

You use registry keys to associate a directory class name with the ADSI extension components. The following figure represents the existing registry layout, as a well as new keys.

-   A new key, called **Extensions**, contains a list of keys, each of which represents a class in the directory. Each class, for example, **user**, **printQueue**, or **computer**, maintains a list of subkeys.
-   Each subkey contains the CLSID of the ADSI extension component.
-   Each CLSID subkey contains a string entry that allows multiple values. You should only list the interfaces that participate in the aggregation.

> [!Note]  
> Extension objects are still required to register standard COM keys.

 

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         ADS
            Providers
               LDAP
                  Extensions
                     ClassNameA
                        CLSID of ExtensionA1
                           Interfaces = List of interfaces
                        CLSID of ExtensionA2
                           Interfaces = List of interfaces
                     ClassNameB
                        CLSID of ExtensionB1
                           Interfaces = List of interfaces
                        CLSID of ExtensionB2
                           Interfaces = List of interfaces
```

## Example

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         ADs
            Providers
               LDAP
                  Extensions
                     printQueue
                        {9f37f39c-6f49-11d1-8c18-00c04fd8d503}
                           Interfaces = {466841B0-E531-11d1-8718-00C04FD44407}
                                        {466841B1-E531-11d1-8718-00C04FD44407}
```

The list of interfaces from Extension1 can be different from that of Extension2. The object, when active, supports the interfaces of the aggregator (ADSI) and all the interfaces provided by the aggregate's Extension1 and Extension2. Resolution of conflicting interfaces (the same interface supported by both the aggregator and the aggregates or by multiple aggregates) is determined by priorities of the extensions.

You can also associate your CLSID extension with multiple object class names. For example, your extension can extend both the **user** and **contact** objects.

> [!Note]  
> Extension behavior is added on a per-object class, not on a per-object instance.

 

As a best practice, register your extensions, as you would any other COM components, with a call to the **DllRegisterSvr** function. Also provide a facility to unregister your extension with the **DllUnregisterServer** function.

The following code example shows how to register an extension.


```C++
/////
// Register the class.
///////////////////////
hr = RegCreateKeyEx( HKEY_LOCAL_MACHINE,
                 _T("SOFTWARE\\Microsoft\\ADs\\Providers\\LDAP\\Extensions\\User\\{E1E3EDF8-48D1-11D2-B22B-0000F87A6B50}"),
 0,
 NULL,
 REG_OPTION_NON_VOLATILE,
 KEY_WRITE,
 NULL,
 &hKey,
 &dwDisposition );
 
///////////////////////////
// Register the Interface.
///////////////////////////
const TCHAR szIf[] = _T("{E1E3EDF7-48D1-11D2-B22B-0000F87A6B50}");
 
hr = RegSetValueEx( hKey, _T("Interfaces"), 0, REG_BINARY, (const BYTE *) szIf, sizeof(szIf) );
 
RegCloseKey(hKey);
return S_OK;
 
}
```



 

 