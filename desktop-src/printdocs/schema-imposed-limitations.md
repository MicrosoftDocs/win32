---
description: Learn about the limitations imposed by the PrintCapabilities Schema. The PrintCapabilities provider must detect invalid of configurations and resolve them.
ms.assetid: 420c5c84-abb8-495a-9b74-dc19a16034fb
title: Schema-Imposed Limitations
ms.topic: article
ms.date: 05/31/2018
---

# Schema-Imposed Limitations

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

The PrintCapabilities Schema provides PrintCapabilities authors with a substantial amount of flexibility and expressiveness that can be utilized in device descriptions. However, configuration dependencies impose a limitation on this flexibility and expressiveness. ParameterDef instances, the list of Feature elements, the list of Option instances within each Feature, and the ScoredProperty instances within each Option must not contain configuration dependencies. The PrintCapabilities document provider must detect invalid combinations of configurations and must resolve them.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



