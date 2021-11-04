---
title: switch Statement (Urlmon.h)
description: Transfer control to a different statement block within the switch body depending on the value of a selector.
ms.assetid: d1932ee1-d789-4536-b77d-162aacdbb115
keywords:
- switch Statement HLSL
topic_type:
- apiref
api_name:
- switch Statement
api_location:
- urlmon.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# switch Statement

Transfer control to a different statement block within the switch body depending on the value of a selector.


\[*Attribute*\] switch( *Selector* ) {   case 0 :     { *StatementBlock*; }   break;   case 1 :     { *StatementBlock*; }   break;   case n :     { *StatementBlock*; }   break;   default :     { *StatementBlock*; }   break;



 

## Parameters

<dl> <dt>

<span id="Attribute"></span><span id="attribute"></span><span id="ATTRIBUTE"></span>*Attribute*
</dt> <dd>

An optional parameter that controls how the statement is compiled. When no attribute is specified, the compiler may use a hardware switch or emit a series of **if** statements.




| Attribute | Description | 
|-----------|-------------|
| flatten | Compile the statement as a series of <strong>if</strong> statements, each with the <strong>flatten</strong> attribute. | 
| branch | Compile the statement as a series of <strong>if</strong> statements each with the <strong>branch</strong> attribute.<blockquote>[!Note]<br />When you use <a href="dx-graphics-hlsl-sm2.md">Shader Model 2.x</a> or <a href="dx-graphics-hlsl-sm3.md">Shader Model 3.0</a>, each time you use dynamic branching you consume resources. So, if you use dynamic branching excessively when you target these profiles, you can receive compilation errors.</blockquote><br /> | 
| forcecase | Force a switch statement in the hardware.<blockquote>[!Note]<br />Requires <a href="/windows/desktop/direct3d11/overviews-direct3d-11-devices-downlevel-intro">feature level</a> 10_0 or later hardware.</blockquote><br /> | 
| call | The bodies of the individual cases in the switch will be moved into hardware subroutines and the switch will be a series of subroutine calls.<blockquote>[!Note]<br />Requires <a href="/windows/desktop/direct3d11/overviews-direct3d-11-devices-downlevel-intro">feature level</a> 10_0 or later hardware.</blockquote><br /> | 




 

</dd> <dt>

<span id="Selector"></span><span id="selector"></span><span id="SELECTOR"></span>*Selector*
</dt> <dd>

A variable. The case statements inside the curly brackets will each check this variable to see if the SwitchValue matches their particular CaseValue.

</dd> <dt>

<span id="StatementBlock"></span><span id="statementblock"></span><span id="STATEMENTBLOCK"></span>*StatementBlock*
</dt> <dd>

One or more [statements](dx-graphics-hlsl-statement-blocks.md).

</dd> </dl>

## Remarks


```
[branch] switch(a)
{
    case 0:
        return 0; 
    case 1:
        return 1; 
    case 2:
        return 3; 
    default:
        return 6; 
}
```



Is equivalent to:


```
[branch] if( a == 2 )
    return 3;
else if( a == 1 )
    return 1;
else if( a == 0 )
    return 0;
else
    return 6;
```



Here are example usages of forcecase and call flow control attributes:


```
[forcecase] switch(a)
{
    case 0:
        return 0; 
    case 1:
        return 1; 
    case 2:
        return 3; 
    default:
        return 6; 
}

[call] switch(a)
{
    case 0:
        return 0; 
    case 1:
        return 1; 
    case 2:
        return 3; 
    default:
        return 6; 
}
```



## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Urlmon.h</dt> </dl> |



## See also

<dl> <dt>

[Flow Control](dx-graphics-hlsl-flow-control.md)
</dt> </dl>

 

