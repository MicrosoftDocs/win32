---
title: Effect Group Syntax (Direct3D 11)
description: An effect group is declared with the syntax described in this section.
ms.assetid: f6695ae5-198f-45bd-853b-8c02fabd0c39
ms.topic: reference
ms.date: 05/31/2018
---

# Effect Group Syntax (Direct3D 11)

An effect group is declared with the syntax described in this section.


```
fxgroup GroupName  [ <Annotations > ]
{
    TechniqueVersion TechniqueName [ <Annotations > ] 
    { 
       ...
    } 
    TechniqueVersion TechniqueName [ <Annotations > ] 
    { 
       ...
    } 
}



```



## Parameters



| Item                                                                                                                                                                           | Description                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="fxgroup"></span><span id="FXGROUP"></span>fxgroup<br/>                                                                                                         | equired keyword.<br/>                                                                                                                                                                                                         |
| <span id="GroupName"></span><span id="groupname"></span><span id="GROUPNAME"></span>GroupName<br/>                                                                       | Required. An ASCII string that uniquely identifies the name of the effect group. Unlike techniques, groups must have names to ensure that techniques have a unique identifier (see Groups and Techniques section below).<br/> |
| <span id="_______________Annotations__"></span><span id="_______________annotations__"></span><span id="_______________ANNOTATIONS__"></span> < Annotations ><br/> | \[in\] Optional. One or more pieces of user-supplied information (metadata) that is ignored by the effect system. For syntax, see Annotation Syntax (Direct3D 11). <br/>                                                      |
| <span id="TechniqueVersion"></span><span id="techniqueversion"></span><span id="TECHNIQUEVERSION"></span>TechniqueVersion<br/>                                           | Either "technique10" or "technique11". Techniques which use functionality new to Direct3D 11 (5\_0 shaders, BindInterfaces, etc) must use "technique11".<br/>                                                                 |
| <span id="TechniqueName"></span><span id="techniquename"></span><span id="TECHNIQUENAME"></span>TechniqueName<br/>                                                       | Optional. An ASCII string that uniquely identifies the name of the effect technique. <br/>                                                                                                                                    |



 

## Groups and Techniques

In order to maintain compatibility with fx\_4\_0 effects, groups are optional. There is an implicit NULL-named group surrounding all global techniques.

Consider the following example:


```
technique11 GlobalTech
{
}
fxgroup Group1
{
     technique11 Tech1 { ... }
     technique11 Tech2 { ... }
}
fxgroup Group2
{
     technique11 Tech1 { ... }
     technique11 Tech2 { ... }
}
```



In C++, one can get a technique by name in two ways. The following commands will find the obvious techniques:


```
pEffect->GetTechniqueByName( "GlobalTech" );
pEffect->GetTechniqueByName( "|GlobalTech" );
pEffect->GetTechniqueByName( "Group1|Tech1" );
pEffect->GetTechniqueByName( "Group1|Tech2" );
pEffect->GetTechniqueByName( "Group2|Tech1" );
pEffect->GetTechniqueByName( "Group2|Tech2" );
pEffect->GetGroupByName("Group1")->GetTechniqueByName( "Tech1" );
pEffect->GetGroupByName("Group1")->GetTechniqueByName( "Tech2" );
pEffect->GetGroupByName("Group2")->GetTechniqueByName( "Tech1" );
pEffect->GetGroupByName("Group2")->GetTechniqueByName( "Tech2" );
```



In order to ensure that [**ID3DX11Effect::GetTechniqueByName**](id3dx11effect-gettechniquebyname.md) works similarly to Effects 10, all defined groups must have a name.

## Related topics

<dl> <dt>

[Effect Format](d3d11-effect-format.md)
</dt> <dt>

[Effect Technique Syntax (Direct3D 11)](d3d11-effect-technique-syntax.md)
</dt> </dl>

 

 





