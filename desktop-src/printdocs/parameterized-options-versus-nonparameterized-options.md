---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 92438df1-afde-4038-853e-9b98f7e589ea
title: Parameterized Options versus Nonparameterized Options
ms.topic: article
ms.date: 05/31/2018
---

# Parameterized Options versus Nonparameterized Options

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

PrintCapabilities and PrintTicket providers must correctly handle parameterized Option instances during the PrintTicket validation process. As discussed in [Option Definitions](option-definitions.md), one step performed in PrintTicket validation is to find the Option in the current device's PrintCapabilities document (the candidate Option) that best matches the Option specified in the PrintTicket (the reference Option). When one or both of the Option instances is parameterized, there are three possible cases that must be handled by the device driver defined scoring process: the case where both Option instances are parameterized, and the two cases where one Option is parameterized and the other is not. In the following cases it is assumed that there is a correspondence between the parameterized ScoredProperty instances in the PrintTicket Option and a particular ScoredProperty in the PrintCapabilities Option. If there is no correspondence, the scoring process can treat these ScoredProperty instances in the same way that it treats any other noncorresponding ScoredProperty instances.

## Case 1 - Parameterized PrintTicket and PrintCapabilities Document Options

In this case, both the reference Option (in the PrintTicket) and the candidate Option (in the PrintCapabilities document) are parameterized. Access the ParameterDef instance that is referenced by the candidate Option (both in the PrintCapabilities document), and determine whether the ParameterInit value specified in the PrintTicket falls into the range allowed by the ParameterDef instance. If so, consider this ScoredProperty to be a match. Otherwise, this ScoredProperty is not a match.

## Case 2 - Parameterized PrintTicket Option, Nonparameterized PrintCapabilities Document Option

In this case, the PrintTicket contains a Feature with a parameterized Option, while the corresponding Feature in the PrintCapabilities document contains at least one Option that is not parameterized. Even if the PrintCapabilities document also contains other Option instances that are parameterized, the scoring process must be applied to every Option, because the goal is to identify the best matching Option. The client must be able to compare nonparameterized Option candidates with a reference Option that is parameterized.

Because the parameterized Option appears in the PrintTicket, the ParameterInit instances should also be present as illustrated in the previous case. The scoring process can simply replace any ParameterRef instance in the PrintTicket's parameterized Option with the Value specified by the PrintTicket's ParameterInit instance. This effectively converts a parameterized Option into one that is not parameterized. At this point the conventional matching process can be used.

## Case 3 - Nonparameterized PrintTicket Option, Parameterized PrintCapabilities Document Option

In this case, the reference Option in the PrintTicket is not parameterized, while the candidate Option in the PrintCapabilities document is parameterized. Access the ParameterDef instance in the PrintCapabilities document that is referenced by the candidate Option's ParameterRef instance in the PrintTicket, and determine whether the Value defined in the reference Option for the corresponding ScoredProperty falls into the range allowed by the ParameterDef instance. If so, consider this ScoredProperty to be a match. If not, this ScoredProperty is not a match.

It should be emphasized that you make the determination of how closely two Option instances match by the number (and significance) of the ScoredProperty instances that match, independent of whether the ScoredProperty instances contain explicit Value instances or ParameterRef instances. It is possible for a candidate Option to be the best match, even though it contains several Property instances that do not match those of the reference Option, or that have no corresponding Property in the reference Option.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



