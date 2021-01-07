---
description: The following lists standard qualifiers specific to WMI.
ms.assetid: 63bdbafc-51f3-4714-8b7e-9d5a61cef45e
ms.tgt_platform: multiple
title: Standard WMI Qualifiers
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Standard
api_type: 
- NA
api_location: 
---

# Standard WMI Qualifiers

The following lists standard qualifiers specific to WMI.

<dt>

<span id="Amendment"></span><span id="amendment"></span><span id="AMENDMENT"></span>**Amendment**
</dt> <dd>

Data type: **boolean**

Applies to: classes

Indicates that a class contains amended qualifiers that are localized. The default is **TRUE**.

The associated class can be translated. To access the translated version, use the locale identifier to construct a namespace name.

</dd> <dt>

<span id="Bypass_GetObject"></span><span id="bypass_getobject"></span><span id="BYPASS_GETOBJECT"></span>**Bypass\_GetObject**
</dt> <dd>

Data type: **boolean**

Applies to: methods

Indicates that the method call should pass directly to the **ExecMethodAsync** call of the provider rather than the provider first making a call to **GetObject** to validate the object path. The default is **FALSE**. Using **Bypass\_GetObject** can significantly improve performance.

Before using **Bypass\_GetObject**, ensure that neither of the following actions are taken:

-   Derive a class from your class.
-   Override the method that has the **Bypass\_GetObject** qualifier.

Failure to follow these precautions can result in invoking the method implementation of the parent class instead of the child class. For more information, see Using the Bypass\_GetObject Qualifier.

</dd> <dt>

<span id="CIM_Key"></span><span id="cim_key"></span><span id="CIM_KEY"></span>**CIM\_Key**
</dt> <dd>

Data type: **CIM\_BOOLEAN**

Applies to: properties

Indicates that the associated property is a key property in CIM but not in WMI.

</dd> <dt>

<span id="CIMType"></span><span id="cimtype"></span><span id="CIMTYPE"></span>[**CIMType**](cimtype-qualifier.md)
</dt> <dd>

Data type: **VT\_BSTR**

Applies to: properties, methods, parameters

Contains text describing the type of a property.

</dd> <dt>

<span id="ClassContext"></span><span id="classcontext"></span><span id="CLASSCONTEXT"></span>**ClassContext**
</dt> <dd>

Data type: **VT\_BSTR**

Applies to: classes

Indicates that a class has instances associated with more information dynamically supplied by a provider.

</dd> <dt>

<span id="Deprecated"></span><span id="deprecated"></span><span id="DEPRECATED"></span>**Deprecated**
</dt> <dd>

Data type: **CIM\_BOOLEAN**

Applies to: properties, classes

Indicates the property has been superseded by another property.

</dd> <dt>

<span id="Display"></span><span id="display"></span><span id="DISPLAY"></span>**Display**
</dt> <dd>

Applies to: classes, properties

The **UUID** of the associated class.

</dd> <dt>

<span id="Dynamic"></span><span id="dynamic"></span><span id="DYNAMIC"></span>[**Dynamic**](dynamic-qualifier.md)
</dt> <dd>

Data type: **boolean**

Applies to: classes, properties

Indicates a class whose instances are created dynamically. The value of this qualifier must be set to **TRUE**.

</dd> <dt>

<span id="DynProps"></span><span id="dynprops"></span><span id="DYNPROPS"></span>**DynProps**
</dt> <dd>

Data type: **boolean**

Applies to: classes, instances

Indicates that an instance contains values provided by dynamic property providers. The default is **TRUE**.

You must specify this qualifier on such an instance. Only the value **TRUE** is allowed.

</dd> <dt>

<span id="Fixed"></span><span id="fixed"></span><span id="FIXED"></span>**Fixed**
</dt> <dd>

Data type: **CIM\_BOOLEAN**

Applies to: instances

Indicates that the value of this property cannot change during the lifetime of the instance.

</dd> <dt>

<span id="ID"></span><span id="id"></span>**ID**
</dt> <dd>

Data type: **VT\_I4**

Applies to: properties, parameters

Uniquely identifies and sequences a property or method parameter when MOF statements are generated automatically.

This qualifier is required for method parameters only. When creating parameters for a method, class designers should begin with Id(0) for the first parameter and use each successive integer for each successive parameter. If the **ID** qualifiers are unintentionally omitted, the MOF compiler generates **ID** qualifiers automatically.

</dd> <dt>

<span id="Implemented"></span><span id="implemented"></span><span id="IMPLEMENTED"></span>**Implemented**
</dt> <dd>

Data type: **boolean**

Applies to: methods

Indicates that a method has an implementation supplied by a provider.

</dd> <dt>

<span id="InstanceContext"></span><span id="instancecontext"></span><span id="INSTANCECONTEXT"></span>**InstanceContext**
</dt> <dd>

Data type: **VT\_BSTR**

Applies to: instances

Indicates that an instance contains values provided by a dynamic property provider.

The value is passed to the property provider as an argument to the [**IWbemPropertyProvider::GetProperty**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbempropertyprovider-getproperty) method.

</dd> <dt>

<span id="Locale"></span><span id="locale"></span><span id="LOCALE"></span>**Locale**
</dt> <dd>

Data type: **VT\_BSTR**

Applies to: classes or instances

Specifies the language of origin for a class or instance. For more information about locale values, see [Locale Codes](#locale-codes).

</dd> <dt>

<span id="NamespaceSecuritySDDL"></span><span id="namespacesecuritysddl"></span><span id="NAMESPACESECURITYSDDL"></span>**NamespaceSecuritySDDL**
</dt> <dd>

Data type: **string array**

Applies to: namespace instances

Specifies a security descriptor for the namespace in [SDDL](/windows/desktop/SecAuthZ/security-descriptor-definition-language) format. For more information, see [Setting Namespace Security When the Namespace is Created](setting-namespace-security-when-the-namespace-is-created.md). The SDDL string is processed by WMI to establish the namespace security but not stored as a string. If no security descriptor is specified, the default security is used. For more information, see [Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md).

</dd> <dt>

<span id="Optional"></span><span id="optional"></span><span id="OPTIONAL"></span>**Optional**
</dt> <dd>

Data type: **boolean**

Applies to: parameters

Indicates that a parameter is not required, and that it has a well-behaved default value.

</dd> <dt>

<span id="Privileges"></span><span id="privileges"></span><span id="PRIVILEGES"></span>**Privileges**
</dt> <dd>

Data type: **string array**

Applies to: properties, methods

Set of values used to inform the client which privileges are required to create instances, fill in properties, or perform methods. The default is **FALSE**.

</dd> <dt>

<span id="PropertyContext"></span><span id="propertycontext"></span><span id="PROPERTYCONTEXT"></span>**PropertyContext**
</dt> <dd>

Data type: **VT\_BSTR**

Applies to: properties

Indicates that an instance property contains values provided by dynamic property providers.

You must specify this qualifier on such a property. The value is passed to the property provider as an argument to [**IWbemPropertyProvider::GetProperty**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbempropertyprovider-getproperty).

</dd> <dt>

<span id="Provider"></span><span id="provider"></span><span id="PROVIDER"></span>**Provider**
</dt> <dd>

Data type: **VT\_BSTR**

Applies to: classes

The value of this qualifier is the name of the dynamic provider that provides class instances and refreshes instance data. This name must be registered with WMI by creating an instance of the [**\_\_Win32Provider**](--win32provider.md) class with the **Name** property containing this name. When this qualifier is specified on a class whose instances are provided dynamically, the **Dynamic** qualifier must also be specified.

</dd> <dt>

<span id="RequiresEncryption"></span><span id="requiresencryption"></span><span id="REQUIRESENCRYPTION"></span>**RequiresEncryption**
</dt> <dd>

Data type: **boolean**

Applies to: namespace instances

If set to **TRUE**, **RequiresEncryption** marks a namespace so that client applications and scripts must connect with encrypted authentication. The authentication level must be set to **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY** in C++. In scripting or Visual Basic, authentication level must be set to **WbemAuthenticationLevelPktPrivacy**. For more information, see [Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md). The qualifier is used in [*MOF*](gloss-m.md) with the pragma namespace preprocessor command.

For more information, see [Setting the Default Process Security Level Using C++](setting-the-default-process-security-level-using-c-.md) or [Setting the Default Process Security Level Using VBScript](setting-the-default-process-security-level-using-vbscript.md). Scripting authentication levels are defined in [**WbemAuthenticationLevelEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemauthenticationlevelenum).

</dd> <dt>

<span id="Singleton"></span><span id="singleton"></span><span id="SINGLETON"></span>**Singleton**
</dt> <dd>

Data type: **boolean**

Applies to: classes

Designates a class that can only have one instance and that does not contain key properties.

Only the value **TRUE** (default) is allowed.

</dd> <dt>

<span id="Static"></span><span id="static"></span><span id="STATIC"></span>**Static**
</dt> <dd>

Data type: **boolean**

Applies to: methods

Indicates whether a method can called by using the class definition or its instances.

The method cannot be invoked from an instance.

</dd> <dt>

<span id="SubType"></span><span id="subtype"></span><span id="SUBTYPE"></span>**SubType**
</dt> <dd>

Data type: **VT\_BSTR**

Applies to: properties

Indicates that a property of type **CIM\_DATETIME** represents a time interval rather than a specific time.

To identify the property as an interval, the value of this qualifier must be "interval". All other values for this qualifier are reserved for future use.

</dd> <dt>

<span id="UUID"></span><span id="uuid"></span>**UUID**
</dt> <dd>

Data type: **string**

Applies to: classes

Universally unique identifier applied to the class.

</dd> <dt>

<span id="ClassVersion"></span><span id="classversion"></span><span id="CLASSVERSION"></span>**ClassVersion**
</dt> <dd>

Data type: **string**

Applies to: classes

The version number of the class object. The default is **NULL**. The version number is incremented when changes are made to the class.

</dd> <dt>

<span id="WritePrivileges"></span><span id="writeprivileges"></span><span id="WRITEPRIVILEGES"></span>**WritePrivileges**
</dt> <dd>

Data type: **string array**

Applies to: properties

Set of values indicating which system privileges must be available and enabled for a successful write operation.

</dd> </dl>

## Remarks

### Locale Codes

A locale code is of the form "MS\_<Three Digit Language ID>". For example, English locale is MS\_409. The following table lists the language IDs.



| Language              | Language ID (hexadecimal) |
|-----------------------|---------------------------|
| Arabic                | 401                       |
| Portuguese (Brazil)   | 416                       |
| Chinese (Simplified)  | 804                       |
| Chinese (Traditional) | 404                       |
| Czech                 | 405                       |
| Danish                | 406                       |
| Dutch                 | 413                       |
| English (default)     | 409                       |
| Finnish               | 40b                       |
| French                | 40c                       |
| German                | 407                       |
| Greek                 | 408                       |
| Hebrew                | 40d                       |
| Hungarian             | 40e                       |
| Italian               | 410                       |
| Japanese              | 411                       |
| Korean                | 412                       |
| Norwegian             | 414                       |
| Polish                | 415                       |
| Portuguese (Portugal) | 816                       |
| Russian               | 419                       |
| Spanish               | c0a                       |
| Swedish               | 41D                       |
| Turkish               | 41f                       |



 

### Using the Bypass\_GetObject Qualifier

Using the **Bypass\_GetObject** qualifier on a method can produce confusing results.

The following example defines the **Shape** and **Circle** classes. Note that the **Circle** class is derived from the **Shape** class.


```VB
class Shape
{
   string Name;
   uint32 DrawIt();  // - draws an irregular geometric shape
};

class Circle : Shape
{
   uint32 DrawIt();  // - draws a circle
};
```



The following call to **ExecMethod** uses a **Circle** object named "MyCircle" to draw a circle.


```VB
ExecMethod("Shape.Name='MyCircle'","DrawIt");
```



In the previous scenario, WMI calls **GetObject**; discovers that "Shape.Name='MyCircle'" is a **Circle**; and executes the **Circle** implementation of **DrawIt**. However, if you use the **Bypass\_GetObject** qualifier on **DrawIt**, WMI does not call **GetObject**, does not discover that "Shape.Name='MyCircle'" is a **Circle**, and executes the **Shape** implementation of **DrawIt** instead of the **Circle** implementation of **DrawIt**.

The following call to **ExecMethod** always invokes the correct implementation of **DrawIt**.


```VB
ExecMethod("Circle.Name='MyCircle'","DrawIt");
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md)
</dt> <dt>

[WMI Qualifiers](wmi-qualifiers.md)
</dt> <dt>

[Adding a Qualifier](adding-a-qualifier.md)
</dt> </dl>

 

