---
description: A conditional access control entry (ACE) allows an access condition to be evaluated when an access check is performed. The security descriptor definition language (SDDL) provides syntax for defining conditional ACEs in a string format.
ms.assetid: cdc3629d-c4d8-4910-8838-3bdb601f7064
title: Security Descriptor Definition Language for Conditional ACEs
ms.topic: article
ms.date: 05/31/2018
---

# Security Descriptor Definition Language for Conditional ACEs

A conditional [*access control entry*](/windows/desktop/SecGloss/a-gly) (ACE) allows an access condition to be evaluated when an access check is performed. The security descriptor definition language (SDDL) provides syntax for defining conditional ACEs in a string format.

The SDDL for a conditional ACE is the same as for any ACE, with the syntax for the conditional statement appended to the end of the ACE string. For information about SDDL, see [Security Descriptor Definition Language](security-descriptor-definition-language.md).

The "\#" sign is synonymous with "0" in resource attributes. For example, D:AI(XA;OICI;FA;;;WD;(OctetStringType==\#1\#2\#3\#\#)) is equivalent to and interpreted as D:AI(XA;OICI;FA;;;WD;(OctetStringType==\#01020300)).

-   [Conditional ACE String Format](#conditional-ace-string-format)
-   [Conditional Expressions](#conditional-expressions)
-   [Attributes](#attributes)
-   [Operators](#operators)
-   [Operator Precedence](#operator-precedence)
-   [Unknown Values](#unknown-values)
-   [Conditional ACE Evaluation](#conditional-ace-evaluation)
-   [Examples](#examples)
-   [Related topics](#related-topics)

## Conditional ACE String Format

Each ACE in a [*security descriptor*](/windows/desktop/SecGloss/s-gly) string is enclosed in parentheses. The fields of the ACE are in the following order and are separated by semicolons (;).

*AceType***;***AceFlags***;***Rights***;***ObjectGuid***;***InheritObjectGuid***;***AccountSid***;(***ConditionalExpression***)**

The fields are as described in [ACE Strings](ace-strings.md), with the following exceptions.

-   The *AceType* field can be one of the following strings.

    | ACE type string | Constant in Sddl.h                         | AceType value                                   |
    |-----------------|--------------------------------------------|-------------------------------------------------|
    | "XA"<br/> | SDDL\_CALLBACK\_ACCESS\_ALLOWED<br/> | ACCESS\_ALLOWED\_CALLBACK\_ACE\_TYPE<br/> |
    | "XD"<br/> | SDDL\_CALLBACK\_ACCESS\_DENIED<br/>  | ACCESS\_DENIED\_CALLBACK\_ACE\_TYPE<br/>  |

    

     

-   The ACE string includes one or more conditional expressions, enclosed in parentheses at the end of the string.

## Conditional Expressions

A conditional expression can include any of the following elements.



| Expression element                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *AttributeName*<br/>                                        | Tests whether the specified attribute has a nonzero value.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **exists** *AttributeName*<br/>                             | Tests whether the specified attribute exists in the client context.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| *AttributeName* *Operator* *Value*<br/>                     | Returns the result of the specified operation.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| *ConditionalExpression***\|\|***ConditionalExpression*<br/> | Tests whether either of the specified conditional expressions is true.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| *ConditionalExpression* **&&** *ConditionalExpression*<br/> | Tests whether both of the specified conditional expressions are true.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **!(***ConditionalExpression***)**<br/>                     | The inverse of a conditional expression.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Member\_of{***SidArray***}**<br/>                         | Tests whether the [**SID\_AND\_ATTRIBUTES**](/windows/desktop/api/Winnt/ns-winnt-sid_and_attributes) array of the client context contains all of the [Security Identifiers](security-identifiers.md) (SIDs) in the comma-separated list specified by *SidArray*.<br/> For Allow ACEs, a client context SID must have the **SE\_GROUP\_ENABLED** attribute set to be considered a match.<br/> For Deny ACEs, a client context SID must have either the **SE\_GROUP\_ENABLED** or the **SE\_GROUP\_USE\_FOR\_DENY\_ONLY** attribute set to be considered a match.<br/> The *SidArray* array can contain either SID strings (for example, "S-1-5-6") or SID aliases (for example, "BA"<br/> |



 

## Attributes

An attribute represents an element in the [**AUTHZ\_SECURITY\_ATTRIBUTES\_INFORMATION**](/windows/desktop/api/Authz/ns-authz-authz_security_attributes_information) array in the client context. An attribute name can contain any alphanumeric characters and any of the characters ":", "/", ".", and "\_".

An attribute value can be any of the following types.



| Value type         | Description                                                                                                                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Integer<br/> | A 64-bit integer in either decimal or hexadecimal notation.<br/>                                                                                                                              |
| String<br/>  | A string value delimited by quotes.<br/>                                                                                                                                                      |
| SID<br/>     | SID(S-1-1-0) or SID(BA). Has to be on RHS of Member\_of or Device\_Member\_of.<br/>                                                                                                           |
| BLOB<br/>    | \# followed by hexadecimal numbers. If length of the numbers is odd, then the \# is translated to a 0 to make it even. Also an \# appearing elsewhere in the value is translated to a 0.<br/> |



 

## Operators

The following operators are defined for use in conditional expressions to test the values of attributes. All of these are binary operators and used in the form *AttributeName* *Operator* *Value*.



| Operator            | Description                                                                                                              |
|---------------------|--------------------------------------------------------------------------------------------------------------------------|
| ==<br/>       | Conventional definition.<br/>                                                                                      |
| !=<br/>       | Conventional definition.<br/>                                                                                      |
| <<br/>     | Conventional definition.<br/>                                                                                      |
| <=<br/>    | Conventional definition.<br/>                                                                                      |
| ><br/>     | Conventional definition.<br/>                                                                                      |
| >=<br/>    | Conventional definition.<br/>                                                                                      |
| Contains<br/> | **TRUE** if the value of the specified attribute is a superset of the specified value; otherwise, **FALSE**.<br/>  |
| Any\_of<br/>  | **TRUE** if the specified value is a superset of the value of the specified attribute; otherwise, **FALSE**. <br/> |



 

In addition, the unary operators Exists, Member\_of, and negation (!) are defined as described in the Conditional Expressions table.

The "Contains" operator must be preceded and followed by white space, and the "Any\_of" operator must be preceded by white space.

## Operator Precedence

The operators are evaluated in the following order of precedence, with operations of equal precedence being evaluated from left to right.

1.  Exists, Member\_of
2.  Contains, Any\_of
3.  ==, !=, <, <=, >, >=
4.  !
5.  &&
6.  \|\|

In addition, any portion of a conditional expression can be enclosed in parenthesis. Expressions within parentheses are evaluated first.

## Unknown Values

The results of conditional expressions sometimes return a value of **Unknown**. For example, any of the relational operations return **Unknown** when the specified attribute does not exist.

The following table describes the results for a logical **AND** operation between two conditional expressions, *ConditionalExpression1* and *ConditionalExpression2*.



| *ConditionalExpression1* | *ConditionalExpression2* | *ConditionalExpression1* **&&** *ConditionalExpression2* |
|--------------------------|--------------------------|----------------------------------------------------------|
| **TRUE**<br/>      | **TRUE**<br/>      | **TRUE**<br/>                                      |
| **TRUE**<br/>      | **FALSE**<br/>     | **FALSE**<br/>                                     |
| **TRUE**<br/>      | **UNKNOWN**<br/>   | **UNKNOWN**<br/>                                   |
| **FALSE**<br/>     | **TRUE**<br/>      | **FALSE**<br/>                                     |
| **FALSE**<br/>     | **FALSE**<br/>     | **FALSE**<br/>                                     |
| **FALSE**<br/>     | **UNKNOWN**<br/>   | **FALSE**<br/>                                     |
| **UNKNOWN**<br/>   | **TRUE**<br/>      | **UNKNOWN**<br/>                                   |
| **UNKNOWN**<br/>   | **FALSE**<br/>     | **FALSE**<br/>                                     |
| **UNKNOWN**<br/>   | **UNKNOWN**<br/>   | **UNKNOWN**<br/>                                   |



 

The following table describes the results for a logical **OR** operation between two conditional expressions, *ConditionalExpression1* and *ConditionalExpression2*.



| *ConditionalExpression1* | *ConditionalExpression2* | *ConditionalExpression1* **\|\|** *ConditionalExpression2* |
|--------------------------|--------------------------|------------------------------------------------------------|
| **TRUE**<br/>      | **TRUE**<br/>      | **TRUE**<br/>                                        |
| **TRUE**<br/>      | **FALSE**<br/>     | **TRUE**<br/>                                        |
| **TRUE**<br/>      | **UNKNOWN**<br/>   | **TRUE**<br/>                                        |
| **FALSE**<br/>     | **TRUE**<br/>      | **TRUE**<br/>                                        |
| **FALSE**<br/>     | **FALSE**<br/>     | **FALSE**<br/>                                       |
| **FALSE**<br/>     | **UNKNOWN**<br/>   | **UNKNOWN**<br/>                                     |
| **UNKNOWN**<br/>   | **TRUE**<br/>      | **TRUE**<br/>                                        |
| **UNKNOWN**<br/>   | **FALSE**<br/>     | **UNKNOWN**<br/>                                     |
| **UNKNOWN**<br/>   | **UNKNOWN**<br/>   | **UNKNOWN**<br/>                                     |



 

The negation of a conditional expression with a value of **UNKNOWN** is also **UNKNOWN**.

## Conditional ACE Evaluation

The following table describes the access check result of a conditional ACE depending on the final evaluation of the conditional expression.

| ACE type         | TRUE             | FALSE                 | UNKNOWN               |
|------------------|------------------|-----------------------|-----------------------|
| Allow<br/> | Allow<br/> | Ignore ACE<br/> | Ignore ACE<br/> |
| Deny<br/>  | Deny<br/>  | Ignore ACE<br/> | Deny<br/>       |



 

## Examples

The following examples show how the specified access policies are represented by a conditional ACE defined by using SDDL.

<dl> <dt>

<span id="Policy"></span><span id="policy"></span><span id="POLICY"></span>Policy
</dt> <dd>

Allow Execute to Everyone if both of the following conditions are met:

-   Title = PM
-   Division = Finance or Division = Sales

</dd> <dt>

<span id="SDDL"></span><span id="sddl"></span>SDDL
</dt> <dd>

D:(XA; ;FX;;;S-1-1-0; (@User.Title=="PM" && (@User.Division=="Finance" \|\| @User.Division ==" Sales")))

</dd> <dt>

 
</dt> <dd>

 

</dd> <dt>

<span id="Policy"></span><span id="policy"></span><span id="POLICY"></span>Policy
</dt> <dd>

Allow execute if any of the user s projects intersect with the file s projects.

</dd> <dt>

<span id="SDDL"></span><span id="sddl"></span>SDDL
</dt> <dd>

D:(XA; ;FX;;;S-1-1-0; (@User.Project Any\_of @Resource.Project))

</dd> <dt>

 
</dt> <dd>

 

</dd> <dt>

<span id="Policy"></span><span id="policy"></span><span id="POLICY"></span>Policy
</dt> <dd>

Allow read access if the user has logged in with a smart card, is a backup operator, and is connecting from a machine with Bitlocker enabled.

</dd> <dt>

<span id="SDDL"></span><span id="sddl"></span>SDDL
</dt> <dd>

D:(XA; ;FR;;;S-1-1-0; (Member\_of {SID(Smartcard\_SID), SID(BO)} && @Device.Bitlocker))

</dd> <dt>

 
</dt> <dd>

 

</dd> </dl>

## Related topics

<dl> <dt>

[\[MS-DTYP\]: Security Descriptor Description Language](/openspecs/windows_protocols/ms-dtyp/4f4251cc-23b6-44b6-93ba-69688422cb06)
</dt> </dl>

