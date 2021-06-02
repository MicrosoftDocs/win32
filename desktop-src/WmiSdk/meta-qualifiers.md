---
description: Meta qualifiers refine the definition of meta-constructs in the CIM model by clarifying the actual usage of a class or property declaration within the MOF syntax.
ms.assetid: 3674a051-3756-4d09-a70e-46a57b442104
ms.tgt_platform: multiple
title: Meta Qualifiers
ms.topic: reference
ms.date: 05/31/2018
---

# Meta Qualifiers

Meta qualifiers refine the definition of meta-constructs in the CIM model by clarifying the actual usage of a class or property declaration within the MOF syntax.

<dt>

<span id="Association"></span><span id="association"></span><span id="ASSOCIATION"></span>**Association**
</dt> <dd>

Data type: **boolean**

Applies to: classes

Indicates whether the class is an association class used to describe a relationship between two other classes. The absence of this qualifier indicates that the class is not an association class. This qualifier is mutually exclusive with **Indication**. For more information, see [Declaring an Association Class](declaring-an-association-class.md).

</dd> <dt>

<span id="Indication"></span><span id="indication"></span><span id="INDICATION"></span>**Indication**
</dt> <dd>

Data type: **boolean**

Applies to: classes

Indicates whether the object class defines an indication. This qualifier is mutually exclusive with **Association**. The default is **FALSE**.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[WMI Qualifiers](wmi-qualifiers.md)
</dt> <dt>

[Adding a Qualifier](adding-a-qualifier.md)
</dt> </dl>

 

 




