---
Description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 420c5c84-abb8-495a-9b74-dc19a16034fb
title: Schema-Imposed Limitations
ms.topic: article
ms.date: 05/31/2018
---

# Schema-Imposed Limitations

This topic is not current. For the most current information, see the [Print Schema Specification](http://go.microsoft.com/?linkid=7141496).

The PrintCapabilities Schema provides PrintCapabilities authors with a substantial amount of flexibility and expressiveness that can be utilized in device descriptions. However, configuration dependencies impose a limitation on this flexibility and expressiveness. ParameterDef instances, the list of Feature elements, the list of Option instances within each Feature, and the ScoredProperty instances within each Option must not contain configuration dependencies. The PrintCapabilities document provider must detect invalid combinations of configurations and must resolve them.

## Related topics

<dl> <dt>

[Print Schema Specification](http://go.microsoft.com/?linkid=7141496)
</dt> </dl>

 

 



