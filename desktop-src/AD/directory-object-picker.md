---
title: Directory Object Picker
description: The directory object picker dialog box enables a user to select one or more objects from either the global catalog, a domain or computer, or a workgroup.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '5b3e5d71-afd2-49db-b3a2-f9a49f0b2b3a'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Directory Object Picker AD", "object picker AD", "objects AD , object picker"]
---

# Directory Object Picker

The directory object picker dialog box enables a user to select one or more objects from either the global catalog, a domain or computer, or a workgroup. The object types from which a user can select include user, contact, group, and computer objects. For more information about Active Directory Domain Services, see [Active Directory Domain Services](active-directory-domain-services.md).

To display an object picker dialog box:

1.  Call the [**CoCreateInstance**](_com_cocreateinstance) or [**CoCreateInstanceEx**](_com_cocreateinstanceex) function to create an instance of the [**IDsObjectPicker**](idsobjectpicker.md) interface.
2.  Call the [**IDsObjectPicker::Initialize**](idsobjectpicker-initialize.md) method to initialize the dialog box.
3.  Call the [**IDsObjectPicker::InvokeDialog**](idsobjectpicker-invokedialog.md) method to display the dialog box.
4.  Call the [**IDataObject::GetData**](_ole_idataobject_getdata) method of the [**IDataObject**](_ole_idataobject) instance returned by the object picker dialog box to retrieve the [**CFSTR\_DSOP\_DS\_SELECTION\_LIST**](cfstr-dsop-ds-selection-list.md) data. The **CFSTR\_DSOP\_DS\_SELECTION\_LIST** clipboard format provides an **HGLOBAL** that contains a [**DS\_SELECTION\_LIST**](ds-selection-list.md) structure. The **DS\_SELECTION\_LIST** structure contains data about the items selected in the object picker dialog box.

If the Security Identifier (SID) is required for an object, this should be requested directly from the object picker by adding the **objectSID** attribute to the list of attributes to retrieve for the selected object. Passing the returned object name to the [**LsaLookupNames**](https://msdn.microsoft.com/library/windows/desktop/ms721797) or [**LookupAccountName**](https://msdn.microsoft.com/library/windows/desktop/aa379159) function is not recommended because the name lookup will be redundant and may fail in some cases.

If a reference to any selected objects will be saved, the distinguished name should not be saved because the object may move, get renamed, or may change due to locale differences. For security principals, the **objectSID** should be requested for the object and securely saved. If the name of the security principal is needed later, it can be retrieved with the [**LookupAccountSid**](https://msdn.microsoft.com/library/windows/desktop/aa379166) function. For all other objects, the **objectGUID** should be requested and saved.

## Initialization

When the object picker dialog box is initialized, a set of scope types and filters is specified. The specified scope types determine the locations, domains or computers for example, from which a user can select objects. The filters determine the types of objects that a user can select from a given scope type. For more information, see the Scopes and Filters section below.

By default, a user can select a single object in the directory object picker dialog box. To enable multiple selections, set the **DSOP\_FLAG\_MULTISELECT** flag in the **flOptions** member of the [**DSOP\_INIT\_INFO**](dsop-init-info.md) structure when the dialog box initialized.

## Scopes and Filters

The **Look in** drop-down list contains the scopes from which a user can select objects. A scope is a domain, computer, workgroup, or global catalog that stores data about, and provides access to, a set of available objects. The entries in the scope list depend on the scope types and the target computer specified when the [**IDsObjectPicker::Initialize**](idsobjectpicker-initialize.md) method was last called to initialize the object picker dialog box.

A scope type is a generic category of scopes, such as all domains in the enterprise to which the target computer belongs, or the global catalog for the target computer's enterprise, or the target computer itself. For each specified scope type, the dialog box uses the context of the target computer to determine the scope list entries.

The [**IDsObjectPicker::Initialize**](idsobjectpicker-initialize.md) method takes a pointer to a [**DSOP\_INIT\_INFO**](dsop-init-info.md) structure that contains an array of [**DSOP\_SCOPE\_INIT\_INFO**](dsop-scope-init-info.md) structures. Each entry in the **DSOP\_SCOPE\_INIT\_INFO** array specifies one or more scope types as well as applicable filters and other attributes. The filters determine the types of objects, such as users, groups, contacts, and computers, that the user can select from a given scope type. When the user selects a scope from the list, the dialog box applies the filters for that scope type to display a list of objects from which the user can select.

Each [**DSOP\_SCOPE\_INIT\_INFO**](dsop-scope-init-info.md) structure contains a [**DSOP\_FILTER\_FLAGS**](dsop-filter-flags.md) structure that specifies the filters for that scope type. The **DSOP\_FILTER\_FLAGS** structure distinguishes between up-level and down-level scopes:

-   An up-level scope is a global catalog or a domain that supports the ADSI [LDAP provider](https://msdn.microsoft.com/library/aa772203).
-   A down-level scope includes workgroups and all individual computers. The dialog box uses the ADSI WinNT provider to access a down-level scope.

There are two sets of filter flags defined for use in the [**DSOP\_FILTER\_FLAGS**](dsop-filter-flags.md) structure: one for up-level scopes and one for down-level scopes. The **Uplevel** member of the **DSOP\_FILTER\_FLAGS** structure is a [**DSOP\_UPLEVEL\_FILTER\_FLAGS**](dsop-uplevel-filter-flags.md) structure that specifies the filters for up-level scopes. The **flDownlevel** member of the **DSOP\_FILTER\_FLAGS** structure is a set of flags that specify the filters for down-level scopes.

 

 




