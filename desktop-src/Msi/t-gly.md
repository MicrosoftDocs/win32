---
description: Learn about Windows Installer concepts that begin with the letter T, such as transaction processing and transform.
ms.assetid: 06fd0284-5af9-409a-8748-c0b40e0fa317
title: T (Windows Installer)
ms.topic: article
ms.date: 05/31/2018
---

# T (Windows Installer)

[A](a-gly.md) [B](b-gly.md) [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) [F](f-gly.md) [G](g-gly.md) H [I](i-gly.md) J K L [M](m-gly.md) N [O](o-gly.md) [P](p-gly.md) [Q](q-gly.md) [R](r-gly.md) [S](s-gly.md) T [U](u-gly.md) [V](v-gly.md) W X Y Z

<dl> <dt>

<span id="_msi_transaction_processing_gly"></span><span id="_MSI_TRANSACTION_PROCESSING_GLY"></span>**transaction processing**
</dt> <dd>

One or more operations processed together as a single indivisible whole called a transaction. All the constituent operations must succeed for the transaction to succeed, otherwise all the operations are rolled back to the original state.

</dd> <dt>

<span id="_msi_transform_gly"></span><span id="_MSI_TRANSFORM_GLY"></span>**transform**
</dt> <dd>

Template of the differences between two [*installer databases*](i-gly.md) that can be applied to produce similar changes in other databases. For example, a localization transform can be used to change the language of an application. For more information, see [Merges and Transforms](merges-and-transforms.md).

</dd> <dt>

<span id="_msi_transform_error_condition_flags_gly"></span><span id="_MSI_TRANSFORM_ERROR_CONDITION_FLAGS_GLY"></span>**transform error condition flags**
</dt> <dd>

Set of properties used to flag the error conditions of a [*transform*](/windows). For more information, see [**MsiCreateTransformSummaryInfo**](/windows/desktop/api/Msiquery/nf-msiquery-msicreatetransformsummaryinfoa).

</dd> <dt>

<span id="_msi_transform_validation_flags_gly"></span><span id="_MSI_TRANSFORM_VALIDATION_FLAGS_GLY"></span>**transform validation flags**
</dt> <dd>

Set of properties used to verify that the [*transform*](/windows) can be applied to the database. For a list of these properties, see [**MsiCreateTransformSummaryInfo**](/windows/desktop/api/Msiquery/nf-msiquery-msicreatetransformsummaryinfoa).

</dd> </dl>

 

 
