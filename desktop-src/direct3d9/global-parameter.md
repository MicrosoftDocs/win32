---
description: Each DXSAS compliant effect must define, as a minimum, a single global effect parameter with the global semantic.
ms.assetid: 2112db8d-6a11-451d-a9d2-ac1b3cb2da95
title: Global Parameter
ms.topic: article
ms.date: 05/31/2018
---

# Global Parameter

Each DXSAS compliant effect must define, as a minimum, a single global effect parameter with the global semantic. The global parameter can also use one or more optional annotations. The syntax is as follows:


```
int VariableName : SasGlobal
<
    SasVersion 
    [OptionalAnnotations]
>;
```



where:

-   VariableName is a user-specified, ASCII text string variable name.
-   SasGlobal is the semantic keyword that identifies this parameter as the global DXSAS parameter.
-   SasVersion is the only required annotation.
-   OptionalAnnotations can include the following:
    -   [SasEffectAuthor](#saseffectauthor)
    -   [SasEffectAuthoringSoftware](#saseffectauthoringsoftware)
    -   [SasEffectCategory](#saseffectcategory)
    -   [SasEffectCompany](#saseffectcompany)
    -   [SasEffectDescription](#saseffectdescription)
    -   [SasEffectHelp](#saseffecthelp)
    -   [SasEffectRevision](#saseffectrevision)

## SasVersion

The only required annotation is SasVersion. It is declared like this:


```
int3 SasVersion = { major, minor, revision };
```



where:

-   major indicates the DXSAS major release. Major releases of DXSAS can contain sweeping changes to the set of semantics and annotations defined. Semantics and annotations can be added and removed and, in general, backward compatibility with previous releases is not guaranteed.
-   minor indicates the SAS minor release. Minor releases of DXSAS can include the addition of new semantics or annotations. Additionally, semantics and annotations may be marked as deprecated in the DXSAS standard. Deprecated semantics and annotations must still be supported by host applications but can emit a warning diagnostic when such a semantic or annotation is used. Minor releases are backward compatible with previous releases.
-   revision indicates the DXSAS revision. Revisions of DXSAS exist only as a means to fix bugs, remove ambiguity, and refine the standard. Revisions to the standard are backward compatible with previous releases.

The current version is 1.0.0. There is no default value for this annotation.

## SasEffectAuthor

This declares the person who created the effect. It is declared like this:


```
string SasEffectAuthor = "value";
```



where value is a string that identifies the effect author. The default is an empty string.

## SasEffectAuthoringSoftware

This declares the software that the effect was authored on. It is declared like this:


```
string SasEffectAuthoringSoftware = "value";
```



where value is a string that identifies the effect authoring software. The default is an empty string.

## SasEffectCategory

This declares the effect category. It is declared like this:


```
string SasEffectCategory = "value";
```



where value is a string that identifies the effect category. The default is an empty string. The category is expressed via a path-like value using the forward slash as a delimiter. Effects can only belong to one category as there is no syntax for expressing inclusion in multiple paths within a single SasEffectCategory value. The value of this annotation is not treated as case-sensitive by the host application.

## SasEffectCompany

This declares the company that created the effect. It is declared like this:


```
string SasEffectCompany = "value";
```



where value is a string that identifies the name of the company that owns the effect. The default is an empty string.

## SasEffectDescription

This describes the effect. It is declared like this:


```
string SasEffectDescription = "value";
```



where value is a string that describes the effect. The default is an empty string.

## SasEffectHelp

This is a help string that can be displayed to the user whenever help on the associated effect is requested. It is declared like this:


```
string SasEffectHelp = "value";
```



where value is a string that can be displayed if the user requests help. The default is an empty string.

## SasEffectRevision

This annotation allows tools and users to record the revision number of the associated effect file. For example, users could insert appropriate keywords in the value of this annotation to invoke keyword substitution in their favorite revision control software. It is declared like this:


```
string SasEffectRevision = "value";
```



where value is a string that identifies the effect revision. The default is an empty string.

## Examples

Here is an example that uses only the single, required annotation:


```
int gp : SasGlobal
<
  int3 SasVersion = {1,0,0};
>;
```



Here is an example that uses the required annotation and several optional annotations:


```
int gp : SasGlobal
<
  int3 SasVersion = {1,0,0};
  string SasEffectAuthor = "Mike's Shader";
  string SasEffectAuthoringSoftware = "fxe 2.5.4";
  string SasEffectCategory = "/surface/procedural/wood";
  string SasEffectCompany = "Microsoft Corporation";
  string SasEffectDescription = "Renders an irridescent surface.";
  string SasEffectHelp = "For more information, see https://somelocation/skin.htm";    
  string SasEffectRevision = "$Revision$";  
>;
```



## Related topics

<dl> <dt>

[DirectX Standard Annotations and Semantics Reference](dx9-graphics-reference-effects-dxsas.md)
</dt> </dl>

 

 



