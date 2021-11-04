---
description: Review the PrintTicket validation checklist. This topic isn't current. For the most current information, see the Print Schema Specification.
ms.assetid: 4698f151-2237-4d16-b32f-4d15024cd063
title: PrintTicket Validation Checklist
ms.topic: article
ms.date: 05/31/2018
---

# PrintTicket Validation Checklist

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

PrintTicket providers must validate the PrintTicket prior to using it for any purpose. After the PrintTicket is validated, it may be returned to the client, or it may be discarded after use. This checklist covers the tasks the provider must perform during validation. The validation process will frequently alter the content of the PrintTicket, although it will not alter a previously-validated PrintTicket.

Validation is always performed against a specific device that has a set of Feature, Option and ParameterDef instances defined in a PrintCapabilities document. The validation code should have access to the set of Feature instances (and the contained Option instances) and ParameterDef instances for the specific device, and should not need to access the PrintCapabilities. The information from the Feature, Option, and ParameterDef instances is needed in certain parts of the validation process.

1.  During attempts to locate corresponding or matching elements, note that the namespaces of the elements must match before any Qualified Name can be considered a match. All element names, Attribute names, and instance names are namespace-qualified. For elements that are nested, their locations must match before the elements are considered a match.

2.  Verify that all element tags are in the public namespace, are defined by the PrintTicket Schema, contain the proper XML Attributes and Attribute Values, and that the location of each element type conforms to the PrintTicket Schema-defined usage.

3.  Determine all namespaces reported by PrintCapabilities document. Remove all elements (and their descendants) from the PrintTicket whose instance names belong to namespaces not reported by PrintCapabilities document. Note the difference between this case and the following case, which involves unrecognized instance names within a known namespace.

4.  Due to the fact that the schemas are continually being extended with the addition of new element instance definitions, the validation code should not be written under the assumption that every instance name in a given namespace is known. The validation code cannot treat unrecognized instance names within a known namespace as errors, nor can it delete them from the PrintTicket.

5.  If any element instance has a duplicate sibling that is not permitted by the PrintTicket Schema, keep only the first occurrence and delete the duplicates, including the contents of the duplicated element.

6.  Remove from the PrintTicket any Feature or subfeature (and all its children) that has no corresponding Feature in the PrintCapabilities document.

7.  Check the SelectionType Property defined in the PrintCapabilities document for each of the remaining Feature instances in the PrintTicket. Any Feature whose SelectionType Property is set to PickOne must have exactly one Option instance present in the PrintTicket, while a Feature whose SelectionType Property is PickMany may have more than one. If a PrintTicket Feature has no Option instance, supply the default Option instance. Since you are the provider, you know which Option is the default Option for every Feature.

    For a Feature whose SelectionType Property is PickMany, with more than one Option selected in the PrintTicket, verify that no Option is designated as IdentityOption. If there is, delete every other Option, leaving only the one designated IdentityOption.

8.  Remove any ParameterInit instance in the PrintTicket that has no corresponding ParameterDef instance in the PrintCapabilities document.

    For any other ParameterInit instances in the PrintTicket, verify that the Value for each conforms to the PrintCapabilities document's ParameterDef instance. If a Value is missing, supply the default that is provided in the ParameterDef.

9.  Pair each Option instance in the PrintTicket with an Option listed in the corresponding Feature in the PrintCapabilities document, based on the results of the scoring process. Scoring is the process of finding the Option in the PrintCapabilities document that best matches the Option named in the PrintTicket. For a description of what is taken into account during the scoring process, see [Option Definitions](option-definitions.md). Replace each reference Option in the PrintTicket by the corresponding best matching candidate PrintCapabilities document Option. You may also rank all of the candidates by score and pass this information on to the resolving stage in case a constraint conflict prevents the best matching candidate from being used. In such cases, the resolving process can use the second-best candidate rather than pick another candidate at random.

10. For a Feature whose SelectionType Property is set to PickMany, and that has more than one Option selected in the PrintTicket, verify that no Option is designated as IdentityOption. If such an Option exists, delete every other Option, leaving only the one designated IdentityOption. This step must be performed before and after the scoring process is applied.

    The reason that this step must be performed twice is that it is possible for the scoring process to map multiple reference Option instances to the same candidate Option. If that happens, delete any duplicate Option instances so that the Options listed for a particular PickMany Feature are unique.

11. Add to the PrintTicket any Feature present in the PrintCapabilities document that does not appear in the PrintTicket. For such a Feature, designate the default Option as the selected Option.

12. Determine whether there are any ParameterDef instances that meet all of the following criteria:

    -   The ParameterDef instance appears in the PrintCapabilities document, but not in the PrintTicket.

    -   The Mandatory Property of the ParameterDef instance is set to either Unconditional or Conditional.

    -   The ParameterDef instance is referenced by a ParameterRef instance in the PrintTicket within an Option instance.

    For each such ParameterDef instance in the PrintCapabilities document, add to the PrintTicket a corresponding ParameterInit instance. Set the Value of the newly added ParameterInit instances to the default Value specified by the corresponding ParameterDef instances.

13. Perform constraint conflict detection and modify the configuration to eliminate any such conflicts. This topic does not define a particular process to use to resolve constraint conflicts. You need to decide which Feature or ParameterInit instance can be changed, and an appropriate Option or Value, respectively, to select that has the least impact on the overall intent of the configuration specified in the PrintTicket. As mentioned earlier, you might wish to make use of the mapping score of each Option, and use the Option with the second highest score. To determine which Feature or ParameterInit to change, you might want to define a private Property that the client can add to the PrintTicket. This Property can define a priority for Feature and ParameterInit instances so that the resolver process is informed of which Feature or ParameterInit instances are important to the client (and need to be preserved in the PrintTicket), and which are less important.

14. If the constraint resolution process has caused changes in the PrintTicket to any ParameterRef instances for which the Mandatory Property is set to Conditional, add ParameterInit instances with default Values for those that now appear, and remove any ParameterInit instance for a ParameterRef instance that no longer appears.

15. Remove all Property instances and their contents that appear within Option instances in the PrintTicket. Property elements have no role in the PrintTicket. If the validated Option for a particular Feature perfectly matches the prevalidated Option, transfer all of the Property instances in that Option from the prevalidation PrintTicket to the now-validated PrintTicket, subject to the condition that namespaces of Property instances are registered in the PrintCapabilities document. Note that for two Option instances to be considered a perfect match, for every ScoredProperty found in one Option, there must be a corresponding ScoredProperty in the other Option, and the Values of both ScoredProperty instances must be the same.

16. If your PrintTicket provider recognizes and supports any private or public Property instances that have survived to this point, perform validation on them. Do not delete a Property at this point just because you do not recognize it, it might be intended for another phase of document processing.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



