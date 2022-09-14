---
title: RPC unions
description: Encapsulated and nonencapsulated unions and their format with Remote Procedure Call (RPC).
ms.assetid: de13151a-f4a4-4440-b287-454df4a1e3e1
ms.topic: article
ms.date: 05/31/2018
---

# RPC unions

Both encapsulated and nonencapsulated unions share a common union\_arm\_selector<> format:

``` syntax
union_arms<2>
arm1_case_value<4> offset_to_arm_description<2>
..
armN_case_value<4> offset_to_arm_description<2>
default_arm_description<2>
```

The union\_arms<2> field consists of two parts. If the union is a MIDL 1.0 style union, the upper 4 bits contain the alignment of the union arm (alignment of greatest aligned arm). Otherwise the upper 4 bits are zero. The lower 12 bits contain the number of arms in the union. In other words:

``` syntax
alignment<highest nibble> arm_counter<three lower nibbles>
```

The offset\_to\_arm\_description<2> fields contain a relative signed offset to the arm's type description. However, the field is overloaded with optimization for simple types. For these, the upper byte of this offset field is FC\_MAGIC\_UNION\_BYTE (0x80) and the lower byte of the short is the actual format character type of the arm. As such, there are two ranges for the offset values: "80 *xx*" means that *xx* is a type format string; and everything else within range (80 FF .. 7f FF) means an actual offset. This makes offsets from range <80 00 .. 80 FF > unavailable as offsets. The compiler checks that as of MIDL version 5.1.164.

The default\_arm\_description<2> field indicates the type of union arm for the default arm, if any. If there is no default arm specified for the union then the default\_arm\_description<2> field is 0xFFFF and an exception is raised if the switch\_is value does not match any of the arm case values. If the default arm is specified but empty, then the default\_arm\_description<2> field is zero. Otherwise the default\_arm\_description<2> field has the same semantics as the offset\_to\_arm\_description<2> fields.

The following is a summary:

-   0 - empty default
-   FFFF - no default
-   80xx - simple type
-   other - relative offset

## Encapsulated Unions

An encapsulated union comes from a special union syntax in IDL. Effectively, an encapsulated union is a bundle structure with a discriminant field at the beginning of the structure and the union as the only other member.

``` syntax
FC_ENCAPSULATED_UNION switch_type<1> 
memory_size<2>
union_arm_selector<>
```

An encapsulated union's switch\_type<1> field has two parts. The lower nibble provides the actual switch type, and the upper nibble provides the memory increment to step over that is an amount that the memory pointer must be incremented to skip past the switch\_is field, which includes any padding between the switch\_is() field of the stub-constructed structure and the actual union field.

The memory\_size<2> field is the size of the union only, and is identical to nonencapsulated unions. To obtain the total size of the structure that contains the union, add memory\_size<2> to memory increment to step over, that is to the upper nibble of the switch\_type<1> field, then align by the alignment corresponding to the increment.

## Nonencapsulated Unions

A nonencapsulated union is a typical situation where a union is one argument or field and the switch is another argument or field, respectively.

``` syntax
FC_NON_ENCAPSULATED_UNION switch_type<1> 
switch_is_description<>
offset_to_size_and_arm_description<2>
```

Where:

The switch\_type<1> field is a format character for the discriminant.

The switch\_is\_descriptor<> field is a correlation descriptor and has 4 or 6 bytes depending on whether [**/robust**](/windows/desktop/Midl/-robust) is used. However, for the switch\_is\_description<>, if the union is embedded in a structure, the offset field of the switch\_is\_description<> is the offset to the switch\_is field from the union's position in the structure (not from the beginning of the structure).

The offset\_to\_size\_and\_arm\_description<2> field gives the offset to the union's size and arm description, which is identical to that for encapsulated unions and is shared by all nonencapsulated unions of the same type :

``` syntax
memory_size<2> 
union_arm_selector<>
```

 

 