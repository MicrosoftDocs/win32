---
description: Provides rules for mapping WMI classes to Active Directory.
ms.assetid: 295d3233-5729-4eb0-9fa3-1cf64fef2909
ms.tgt_platform: multiple
title: Mapping Active Directory Classes
ms.topic: article
ms.date: 05/31/2018
---

# Mapping Active Directory Classes

Because Active Directory has a wide variety of possible objects, WMI cannot create a direct one-to-one mapping. Instead, the Directory Services provider uses rules to map classes between the two technologies.

This following sections are discussed in this topic:

-   [Mapping Classes](#mapping-classes)
-   [Mapping Attributes](#mapping-attributes)
-   [Association Classes](#association-classes)

> [!Note]  
> For more information about support and installation of this component on a specific operating system, see [Operating System Availability of WMI Components](operating-system-availability-of-wmi-components.md).

 

## Mapping Classes

The following list describes the guidelines that the Directory Services provider uses to map Active Directory classes to WMI classes:

-   Each abstract class in the Active Directory schema maps to one abstract class in the WMI schema.

    In the WMI schema, each abstract class is prefixed with DS\_. For example, the **person** class from the Active Directory schema maps to the **DS\_person** WMI class.

-   Each nonabstract class from the Active Directory schema maps to the following two classes in the WMI schema:

    -   The first mapped class is prefixed with ADS\_. These are abstract classes, mapped according to the rules below.
    -   The second mapped class is a nonabstract class with the DS\_ name prefix. This class is derived from the ADS\_ abstract class, with the addition of the [**Provider**](/windows/desktop/api/Provider/nl-provider-provider) qualifier.

    For example, the **user** class from the Active Directory schema maps to two classes. The first class is the **ADS\_user** abstract class, mapped according to rules below. The second class is the **DS\_user** nonabstract class. It is derived from **ADS\_user** and has the added [**Provider**](/windows/desktop/api/Provider/nl-provider-provider) qualifier.

-   Unless specified otherwise, the name of a mapped class is the mangled value of the **LDAP-Display-Name** property in the Active Directory class.
-   If the **Sub-Class-Of** property is present on the Active Directory class, the WMI-mapped class is derived from the specified class.

    If the **Sub-Class-Of** property is not present, the WMI-mapped class is derived from the **DS\_LDAP\_Root\_Class** class, as specified in the MOF file.

    > [!Note]  
    > This class has the **ADSIPath** key property, with a type **VT\_BSTR**. This is the unique ADSI path that identifies this instance. Active Directory supports single-inheritance only, so this works.

     

-   A **Dynamic** qualifier of type **VT\_BOOL**, and flavor `WBEM_FLAVOR_FLAG_PROPAGATE_TO_INSTANCE | WBEM_FLAVOR_FLAG_PROPAGATE_TO_DERIVED_CLASS` set to **TRUE** is created for every class. This is a standard WMI qualifier that indicates that instances of this class are provided dynamically.
-   If the class is not abstract, the provider creates a [**Provider**](/windows/desktop/api/Provider/nl-provider-provider) qualifier of type **VT\_BSTR BOOL** and qualifier flavor `WBEM_FLAVOR_FLAG_PROPAGATE_TO_INSTANCE | WBEM_FLAVOR_FLAG_PROPAGATE_TO_DERIVED_CLASS` set to "DS Instance Provider" for every class. This is a standard WMI qualifier that indicates the name of the provider dynamically providing instances of this class.

The rest of the ADSI properties map to class qualifiers and properties as per the following tables. All qualifiers map with a qualifier flag value of `WBEM_FLAVOR_FLAG_PROPAGATE_TO_INSTANCE | WBEM_FLAVOR_FLAG_PROPAGATE_TO_DERIVED_CLASS`.

The following lists mapping information for the Active Directory class, showing the WMI qualifier and WMI qualifier type for each Active Directory property.

<dl> <dt>

**Common-Name**
</dt> <dd>

**CN** (**VT\_BSTR**)

Mapped directly from the string value.

</dd> <dt>

**Default-Object-Category**
</dt> <dd>

**DefaultObjectCategory** (**VT\_BSTR**)

Mapped directly from the string value.

</dd> <dt>

**Default-Security-Descriptor**
</dt> <dd>

**DefaultSecurityDescriptor** (**VT\_BSTR**)

Mapped directly from the string value.

</dd> <dt>

**Governs-Id**
</dt> <dd>

**GovernsId** (**VT\_BSTR**)

Mapped from the string representation of the OID; for example, "{ 1 3 3 6 }".

</dd> <dt>

**Object-Class**
</dt> <dd>

N/A

Not mapped.

</dd> <dt>

**Object-Class-Category**
</dt> <dd>

**ObjectClassCategory** (**VT\_I4**)

Mapped directly from the integer value. In addition, if the value is Abstract(2), then the standard **VT\_BOOL** CIM qualifier, called the **"Abstract"** qualifier, is also created.

</dd> <dt>

**RDN-ATT-ID**
</dt> <dd>

**RDNATTID** (**VT\_BSTR**)

Mapped from the string representation of the OID value; for example, "{ 1 3 3 6 }". In addition, the property identified here is annotated with the standard **Indexed** CIM qualifier set to **TRUE**.

</dd> <dt>

**System-Only**
</dt> <dd>

**SystemOnly** (**VT\_BOOL**)

Mapped directly from the Boolean value.

</dd> </dl>

 

The following lists the Active Directory class properties mapped to WMI class properties.

<dl> <dt>

**May-Contain**
</dt> <dd>

Each property in this list is mapped to a WMI property.

</dd> <dt>

**Must-Contain**
</dt> <dd>

Each property in this list is mapped to a WMI property. The standard **Not\_Null** CIM qualifier is created for each of these.

</dd> <dt>

**System-May-Contain**
</dt> <dd>

Each property in this list is mapped to a WMI property. In addition, each property is annotated with a **System** qualifier, set to **TRUE**.

</dd> <dt>

**System-Must-Contain**
</dt> <dd>

Each property in this list is mapped to a WMI property. The standard **Not\_Null** CIM qualifier is created for each of these. In addition, each property is annotated with a **System** qualifier, set to **TRUE**.

</dd> </dl>

## Mapping Attributes

The Directory Services provider maps each attribute of an Active Directory class to exactly one property of the corresponding WMI class according to the rules in this section. In general, the Directory Services Provider names the WMI property as the mangled version of the **LDAP-Display-Name** value of the Active Directory attribute.

If the Active Directory property **Is-Single-Valued** is **FALSE**, then this WMI property is combined with the OR operator with **CIM\_FLAG\_ARRAY**. Note that each property is tagged with the **VT\_BSTR** qualifier, **ADSyntax**. It represents the underlying Active Directory syntax.

The following table lists the mapping of the Active Directory syntax to the WMI property data type.



| Active Directory element                                      | WMI data type                                                           |
|---------------------------------------------------------------|-------------------------------------------------------------------------|
| [**Access-Point**](/windows/desktop/ADSchema/s-object-access-point)            | **CIM\_STRING**                                                         |
| [**Boolean**](/windows/desktop/ADSchema/s-boolean)                             | **CIM\_BOOLEAN**                                                        |
| **Case Insensitive String**                                   | **CIM\_STRING**                                                         |
| [**Case Sensitive String**](/windows/desktop/ADSchema/s-string-case-sensitive) | **CIM\_STRING**                                                         |
| [**Distinguished Name**](/windows/desktop/ADSchema/s-object-ds-dn)             | **CIM\_STRING**                                                         |
| [**DN-Binary**](/windows/desktop/ADSchema/s-object-dn-binary)                  | Embedded object of class **DN\_With\_Binary** defined below.<br/> |
| [**DN-String**](/windows/desktop/ADSchema/s-object-dn-string)                  | Embedded object of class **DN\_With\_String** defined below.<br/> |
| [**Enumeration**](/windows/desktop/ADSchema/s-enumeration)                     | **CIM\_SINT32**                                                         |
| [**Enumeration**](/windows/desktop/ADSchema/s-enumeration)                     | **CIM\_STRING**                                                         |
| [**Integer**](/windows/desktop/ADSchema/s-integer)                             | **CIM\_SINT32**                                                         |
| [**LargeInteger**](/windows/desktop/ADSchema/s-largeinteger)                   | **CIM\_STRING**                                                         |
| Security Descriptor                                           | Embedded object of class **Uint8Array** defined below.<br/>       |
| Numeric String                                                | **CIM\_STRING**                                                         |
| Object ID                                                     | **CIM\_STRING**                                                         |
| Octet String                                                  | Embedded object of class **Uint8Array** defined below.<br/>       |
| OR Name                                                       | **CIM\_STRING**                                                         |
| Presentation-Address                                          | Embedded object of class **Uint8Array** defined below.<br/>       |
| Print Case String                                             | **CIM\_STRING**                                                         |
| Replica Link                                                  | Embedded object of class **Uint8Array** defined below.<br/>       |
| [**String(Sid)**](/windows/desktop/ADSchema/s-string-sid)                      | Embedded object of class **Uint8Array** defined below.<br/>       |
| Time                                                          | **CIM\_DATETIME**                                                       |
| UTC Coded Time                                                | **CIM\_DATETIME**                                                       |
| Unicode String                                                | **CIM\_STRING**                                                         |



 

The Octet String syntax, which refers to an array of **uint8** values, presents a problem when mapped to WMI because WMI allows properties of types **uint8** and arrays of **uint8**, whereas Active Directory allows properties of type Octet String as well as arrays of Octet String.

The following example shows the Directory Services Provider class that is used to map an array of Octet String type properties.

``` syntax
Class Uint8Array 
{
    uint8 values[];
    uint32 numberOfValues;
};
```

WMI maps all Octet String Active Directory property values to embedded instances of **Uint8Array**. Similarly, WMI maps arrays of Octet String to arrays of embedded **Uint8Array** objects.

The following example shows the classes that are mapped by WMI to DN-Binary and DN-String DS property values.

``` syntax
Class DN_With_String
{
    string dnString;
    string value;
};

Class DN_With_Binary
{
    string dnString;
    uint8 value[];
};
```

The following table lists how WMI maps the rest of the Active Directory attribute interface properties to WMI property qualifiers.



| Active Directory attribute-property name | WMI Qualifier       | Data type    | Mapping information                               |
|------------------------------------------|---------------------|--------------|---------------------------------------------------|
| **Attribute-Syntax**                     | **AttributeSyntax** | **VT\_BSTR** | Mapped from the string representation of the OID. |
| **Common-Name**                          | **CN**              | **VT\_BSTR** | Mapped from the string value.                     |
| **System-Only**                          | **System**          | **VT\_BOOL** | Mapped from the Boolean value.                    |



 

> [!Note]  
> WMI maps all Active Directory qualifiers with the `WBEM_FLAVOR_FLAG_PROPAGATE_TO_INSTANCE | WBEM_FLAVOR_FLAG_PROPAGATE_TO_DERIVED_CLASS` qualifier flavors.

 

## Association Classes

The Directory Service is essentially a hierarchical store of objects. Those objects that can appear at a nonleaf level in the hierarchy are called "containers". The structure of this hierarchy is further controlled by the "Poss-Superiors" and "System-Poss-Superiors" properties of a class in the schema. These, taken together, specify the set of classes whose instances can be contained within an instance of a container class.

The following example models a CIM association as instances of the static association class [**DS\_LDAP\_Class\_Containment**](/previous-versions/windows/desktop/dsprov/ds-ldap-class-containment).

``` syntax
//  DS Class Associations Provider 

// Create a class of which instances are
// provided by this provider

[
  Association : ToInstance,
  dynamic,
  HasClassRefs,
  Provider("Microsoft|DSLDAPClassAssociationProvider|V1.0")
]
class DS_LDAP_Class_Containment
{
    [key, classref{"DS_LDAP_Root_Class"} : ToInstance ToSubClass]
    object Ref ChildClass;

    [key, classref{"DS_LDAP_Root_Class"} : ToInstance ToSubClass] 
    object Ref ParentClass; // The parent DS Class
};


// Create an instance of the provider class for registration
instance of __Win32Provider as $AssociationsProvider
{
    Name = "Microsoft|DSLDAPClassAssociationProvider|V1.0";
    Clsid = "{33831ED4-42B8-11d2-93AD-00805F853771}";
    ImpersonationLevel = 1;
};    

// Specification of the instances and operation
// provided by the provider
instance of __InstanceProviderRegistration
{
    Provider = $AssociationsProvider;
    SupportsGet = TRUE;
    SupportsPut = FALSE;
    SupportsDelete = FALSE;
    SupportsEnumeration = TRUE;
};
```

The association class provider supports the [**GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync) and [**CreateClassEnumAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-createclassenumasync) methods.

 

