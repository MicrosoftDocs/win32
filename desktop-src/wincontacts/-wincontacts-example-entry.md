---
title: Programming Windows Contacts
description: This topic provides practical programming examples using the Windows Contacts  API.
ms.assetid: 94a79ca6-4579-433e-abdb-7354c1471048
keywords:
- Windows Contacts,examples
- Windows Contacts,programming examples
- Windows Contacts,backward compatibility
- Windows Contacts,creating contacts
- Windows Contacts,reading contacts
- Windows Contacts,writing contacts
- Windows Contacts,adding labels to properties
- Windows Contacts,adding properties to contacts
- creating contacts
- reading contacts
- writing contacts
- adding labels to properties
- adding properties to contacts
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Programming Windows Contacts

This topic provides practical programming examples using the Windows Contacts  API.

New applications should not use these interfaces. These interfaces exist for backward compatibility with legacy applications. These interfaces will be unavailable in the future.

> [!Note]  
> To save space, these examples do not test the HRESULT code returned by methods. Additionally, they do not test for NULL pointers. In your own programming code always test these values.

 

This topic contains the following examples:

-   [Creating a New Contact](#creating-a-new-contact)
-   [Reading and Writing in an Existing Contact](#reading-and-writing-in-an-existing-contact)
-   [Adding Your Own Label to a Property](#adding-your-own-label-to-a-property)
-   [Adding Your Own Property to a Contact](#adding-your-own-property-to-a-contact)

## Creating a New Contact

This example uses [**IContact**](/windows/previous-versions/icontact/nn-icontact-icontact?branch=master) and [**IContactProperties**](/windows/previous-versions/icontact/nn-icontact-icontactproperties?branch=master) to create a new Contact, enter a value for its Title property, and save it to file. For a list of the application-supplied properties, see [Windows Contact Schema](-wincontacts-schema-entry.md).


```C++
#include <icontact.h>
#include <icontactproperties.h>
#include <objbase.h>  // for IID_PPV_ARGS
#include <smarttypes.h>

#define FILE_NEWCONTACT L"newcontact.contact"

HRESULT CreateNewContact(IClassFactory* pFactory)
{
  HRESULT hr = S_OK;
  IContact* pContact = NULL;
  IContactProperties* pContactProperties = NULL;
  IPersistStreamInit* pPersistInit = NULL;
  IStream* pFileStream = NULL;

  // Create a new contact and initialize it.
  pFactory->CreateInstance(NULL, IID_PPV_ARGS(&amp;pContact));
  pContact->QueryInterface(IID_PPV_ARGS(&amp;pPersistInit));
  pPersistInit->InitNew();

  // Get an IContactProperties interface...
  pContact->QueryInterface(IID_PPV_ARGS(&amp;pContactProperties));
  // ...and use it to set the string value of Title in the first Name property.
  pContactProperties->SetString(CONTACTPROP_PUB_L1_NAMECOLLECTION CONTACTPROP_PUB_L2_NAME L"[1]" 
    CONTACTPROP_PUB_TITLE, CGD_DEFAULT, L"NEW CONTACT");

  // If contact file exists, delete it. Then...
  DeleteFileW(FILE_NEWCONTACT);
  // ...create a new file opened for write, and return an IStream interface.
  SHCreateStreamOnFileEx(
    FILE_NEWCONTACT, STGM_WRITE, FILE_ATTRIBUTE_NORMAL, TRUE, NULL, &amp;pFileStream);

  // Save new contact to file.
  pPersistInit->Save(pFileStream, FALSE);
  
  // Release interface pointers.
  SafeRelease(pFileStream);
  SafeRelease(pContactProperties);
  SafeRelease(pPersistInit);
  SafeRelease(pContact);
  return S_OK;
}
```



## Reading and Writing in an Existing Contact

This example uses [**IContactProperties**](/windows/previous-versions/icontact/nn-icontact-icontactproperties?branch=master) to open an existing Contact, read an existing property, and write a new property value. This example also demonstrates attempting to read a nonexistent Contact property.

> [!Note]  
> To retrieve the value from a multi-value (hierarchical) property, this example includes the desired index as part of the property name in the form: toplevel/secondlevel\[1\]/thirdlevel. The first element of a set is at index 1.

 


```C++
#include <icontact.h>
#include <icontactproperties.h>
#include <smarttypes.h>
#include <objbase.h>  // for IID_PPV_ARGS
#include <windef.h>   // for MAX_PATH
#include <ntdef.h>    // for ARRAYSIZE
#include <stdio.h>    

HRESULT ReadWriteExistingContact(IContact* pContact)
{
  HRESULT hr = S_OK;
  IContactProperties* pContactProp = NULL;
  pContact->QueryInterface(IID_PPV_ARGS(&amp;pContactProp));

  // Read the contact Title and print it to screen.
  WCHAR szTitle[MAX_PATH] = {0};
  pContactProp->GetString(CONTACTPROP_PUB_L1_NAMECOLLECTION CONTACTPROP_PUB_L2_NAME L"[1]"
    CONTACTPROP_PUB_L3_TITLE, CGD_DEFAULT, szTitle, ARRAYSIZE(szTitle), NULL);
  wprintf("The contact Title is: %s \n", szTitle);

  // Set the contact Nickname.
  pContactProp->SetString(CONTACTPROP_PUB_L1_NAMECOLLECTION CONTACTPROP_PUB_L2_NAME L"[1]"
    CONTACTPROP_PUB_NICKNAME, CGD_DEFAULT, L"Bubba");

  // Read the Nickname that was just set and print it to screen.
  WCHAR szNickName[MAX_PATH] = {0};
  pContactProp->GetString(CONTACTPROP_PUB_L1_NAMECOLLECTION CONTACTPROP_PUB_L2_NAME L"[1]"
    CONTACTPROP_PUB_L3_NICKNAME, CGD_DEFAULT, szNickName, ARRAYSIZE(szNickName), NULL);
  wprintf("The contact Nickname is: %s \n", szNickName);

  // Now, try to read a non-existent property.
  WCHAR szFake[MAX_PATH];
  hr = pContactProp->GetString(
    L"FakePropertyNonExistent", CGD_DEFAULT, szFake, ARRAYSIZE(szFake), NULL);
  Assert(HRESULT_FROM_WIN32(ERROR_PATH_NOT_FOUND) == hr);

  // Commit the changes.
  pContact->CommitChanges(CGD_DEFAULT);

  // Release interface pointers.
  SafeRelease(pContactProp);
  return S_OK;
}
```



## Adding Your Own Label to a Property

This example uses [**IContactProperties**](/windows/previous-versions/icontact/nn-icontact-icontactproperties?branch=master) to add a unique outside label to an existing property of an existing contact. This approach assumes that the text of the label is contained in the specified Uniform Resource Identifier (URI).


```C++
#include <icontact.h>
#include <objbase.h>  // for IID_PPV_ARGS
#include <ntdef.h>    // for ARRAYSIZE
#include <smarttypes.h>

#define CONTACTLABEL_3RD_PRIVATE  L"http://schemas.microsoft.com/contact/extensions/labels/private_label"

HRESULT AddLabel(IContact* pContact, LPCWSTR pszProperty)
{
  HRESULT hr = S_OK;
  IContactProperties* pContactProp = NULL;

  pContact->QueryInterface(IID_PPV_ARGS(&amp;pContactProp));

  // Create a unique 3rd-party label as a URI.
  LPCWSTR ppszLabel[] = { CONTACTLABEL_3RD_PRIVATE };
  pContactProp->SetLabels(pszProperty, 0, ARRAYSIZE(ppszLabel), ppszLabel);
  
  // Commit the changes.
  pContact->CommitChanges(CGD_DEFAULT);

  // Release interface pointers.
  SafeRelease(pContactProp);
  return S_OK;
}
```



## Adding Your Own Property to a Contact

This example uses [**IContactProperties**](/windows/previous-versions/icontact/nn-icontact-icontactproperties?branch=master) to add an outside single-value property to an existing contact. This approach is more complicated; it requires creating a unique namespace and can imply that you supply your own schema.


```C++
#include <icontact.h>
#include <objbase.h>  // for IID_PPV_ARGS
#include <smarttypes.h>

HRESULT ExtendContact(IContact* pContact)
{
  HRESULT hr = S_OK;
  IContactProperties* pContactProp = NULL;
  
  // Get the IContactProperties interface.
  pContact->QueryInterface(IID_PPV_ARGS(&amp;pContactProp));

  // Create a unique 3rd-party contact property "FirstCar" and set its value to "Renault".
  #define CONTACTPROP_3RD_FIRSTCAR  L"[unique3rdextension]FirstCar"
  pContactProp->SetString(CONTACTPROP_3RD_FIRSTCAR, CGD_DEFAULT, L"Renault");
  
  // Commit the changes.
  pContact->CommitChanges(CGD_DEFAULT);

  // Release interface pointers.
  SafeRelease(pContactProp);
  return S_OK;
}
```



 

 




