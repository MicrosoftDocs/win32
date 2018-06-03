---
title: Accessing an Active Directory User Object
description: To access an Active Directory object, you must find a Windows domain controller and then bind to the object in the directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 07dc8bdb-700d-4f83-970c-7cb50267796c
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Accessing an Active Directory User Object

To access an Active Directory object, you must find a Windows domain controller and then bind to the object in the directory.

This section describes how a snap-in accesses a user object's properties and attributes when that displays its own property page.

When MMC displays the property sheet for the selected user object, it calls the [**IExtendPropertySheet2::CreatePropertyPages**](https://www.bing.com/search?q=**IExtendPropertySheet2::CreatePropertyPages**) method of the snap-in. MMC then passes the data object of the selected user object in the *lpIDataObject* parameter during the method call. This data object supports the [**CFSTR\_DSOBJECTNAMES clipboard format**](cfstr-dsobjectnames-clipboard-format.md), which the snap-in can use to retrieve the ADsPath string associated with the selected user object. This string represents the exact location of an Active Directory object within the directory hierarchy and is used for binding to the object.

For more information about how to extract the ADsPath string associated with a particular user object, see [**CFSTR\_DSOBJECTNAMES clipboard format**](cfstr-dsobjectnames-clipboard-format.md).

After the snap-in has the ADsPath string of the selected directory object, the snap-in can use one of several ways to bind to that object. For example, an application can use the [**ADsGetObject**](https://msdn.microsoft.com/library/aa772184) function for the binding operation. The following code example shows how this can be done in a dialog box procedure for an application that implements the [**IExtendPropertySheet2**](/windows/desktop/api/Mmc/nn-mmc-iextendpropertysheet2) interface.


```C++
    case WM_INITDIALOG:
    {
       pThis = reinterpret_cast<CPropPageExt *>
              (reinterpret_cast<PROPSHEETPAGE *>(lParam)->lParam);
       HRESULT hr; 
       IDirectoryObject* pDirObject = NULL;
       hr = ADsGetObject(pThis->m_ObjPath,
                         IID_IDirectoryObject,
                         (void **)&amp;pDirObject);
       // ...
       break;
     }
```



The **m\_ObjPath** member holds a pointer to the ADsPath string of the selected directory object.

As shown in the call to [**ADsGetObject**](https://msdn.microsoft.com/library/aa772184), binding to a directory object requires that you specify the COM interface that you want to use to access the directory object. All ADSI COM objects that represent directory objects have an IADs interface. A COM object that represents a directory object also has other interfaces available, depending on the type of directory object.

User objects also support the [**IDirectoryObject**](https://msdn.microsoft.com/library/aa746355) interface.

To retrieve object attributes, a snap-in can call the [**IDirectoryObject::GetObjectAttributes**](https://msdn.microsoft.com/library/aa746358) method returned in the call to [**ADsGetObject**](https://msdn.microsoft.com/library/aa772184). The **GetObjectAttributes** method takes a number of parameters.

The following code example shows one way to use the **GetObjectAttributes** method. To modify the attributes of a directory object, a snap-in can use the **IDirectoryObject::SetObjectAttributes** method.


```C++
    // Retrieve information about the current user object.
    // Use the IDirectoryObject pointer here.
 
    ADS_ATTR_INFO   *pAttrInfo=NULL;
    ADS_ATTR_INFO   *pAttrInfo1=NULL;
 
    DWORD    dwReturn, dwReturn1;
    LPWSTR   pAttrNames[]={L"employeeID",
                           L"mail",
                           L"physicalDeliveryOfficeName",
                           L"telephoneNumber"};
    LPWSTR   pAttrNames1[]={L"allowedAttributesEffective"};
    
    DWORD   dwNumAttr=sizeof(pAttrNames)/sizeof(LPWSTR);
    DWORD   dwNumAttr1=sizeof(pAttrNames1)/sizeof(LPWSTR);
    
    /////////////////////////////////////////
    // First get the allowedAttributesEffective
    // attribute value. Use this value to determine
    // whether you have the proper permissions
    // to modify the attributes of the current
    // object. If you have the proper
    // permissions, you can enable the edit fields.
    // (The edit fields are disabled by default.)
    ///////////////////////////////////////////
 
    bool b_allowEmployeeChange  = FALSE;
    bool b_allowMailChange      = FALSE;
    bool b_allowOfficeChange    = FALSE;
    bool b_allowTelNumberChange = FALSE;
 
    hr = pDirObject->GetObjectAttributes(pAttrNames1,
                                         dwNumAttr1,
                                         &amp;pAttrInfo1,
                                         &amp;dwReturn1 );
    if (SUCCEEDED(hr))
    {
        // The call can succeed with no attributes returned if
        // you do not have the proper permissions,
        // so verify that all attributes are returned.
        if (dwReturn1 &amp;&amp; pAttrInfo1 &amp;&amp; pAttrInfo1->pszAttrName
            &amp;&amp; _wcsicmp(pAttrInfo1->pszAttrName,
            L"allowedAttributesEffective") == 0)
        {
           if (ADSTYPE_INVALID != pAttrInfo1->dwADsType)
           {
             // Permissions are per-attribute. You must
             // verify that the attribute name is in the array of
             // names returned by the read of
             // allowedAttributesEffective.
 
             // The attributes you want to modify 
             // are: employeeID, mail, 
             // physicalDeliveryOfficeName, telephoneNumber
             for (DWORD i = 0; i < pAttrInfo1->dwNumValues; i++)
             {
                  if (_tcscmp(L"employeeID", pAttrInfo1->
                   pADsValues[i].CaseIgnoreString) == 0)
                     b_allowEmployeeChange = TRUE;
 
                  else if (_tcscmp(L"mail", pAttrInfo1->
                         pADsValues[i].CaseIgnoreString) == 0)
                     b_allowMailChange = TRUE;
 
                  else if (_tcscmp(L"physicalDeliveryOfficeName",
                         pAttrInfo1->
                         pADsValues[i].CaseIgnoreString) == 0)
                     b_allowOfficeChange = TRUE;
 
                else if (_tcscmp(L"telephoneNumber", pAttrInfo1
                         ->pADsValues[i].CaseIgnoreString) == 0)
                     b_allowTelNumberChange = TRUE;
              }
           }
        }
    }
 
    // ...
    /////////////////////////////////////////////////////////////
    // Use FreeADsMem for all memory obtained from the ADSI call.
    /////////////////////////////////////////////////////////////
    if (pAttrInfo1)
        FreeADsMem(pAttrInfo1);

    // Release the IDirectoryObject interface
     pDirObject->Release();
```



 

 




