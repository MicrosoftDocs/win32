---
description: Direct3D 10 supports several different floating-point representations. All floating-point computations operate under a defined subset of the IEEE 754 32-bit single precision floating-point behavior.
ms.assetid: 57221d13-8993-4db3-b1a0-88bdcf6f0167
title: FFloating-point rules (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Floating-point rules (Direct3D 10)

Direct3D 10 supports several different floating-point representations. All floating-point computations operate under a defined subset of the IEEE 754 32-bit single precision floating-point behavior.

-   [32-bit Floating-Point Rules](#32-bit-floating-point-rules)
    -   [Honored IEEE-754 Rules](#honored-ieee-754-rules)
    -   [Deviations or Additional Requirements from IEEE-754 Rules](#deviations-or-additional-requirements-from-ieee-754-rules)
-   [16-bit Floating-Point Rules](#16-bit-floating-point-rules)
-   [11-bit and 10-bit Floating-Point Rules](#11-bit-and-10-bit-floating-point-rules)
-   [Related topics](#related-topics)

## 32-bit Floating-Point Rules

There are two sets of rules: those that conform to IEEE-754, and those that deviate from the standard.

### Honored IEEE-754 Rules

Some of these rules are a single option where IEEE-754 offers choices.

-   Divide by 0 produces +/- INF, except 0/0 which results in NaN.
-   log of (+/-) 0 produces -INF. log of a negative value (other than -0) produces NaN.
-   Reciprocal square root (rsq) or square root (sqrt) of a negative number produces NaN. The exception is -0; sqrt(-0) produces -0, and rsq(-0) produces -INF.
-   INF - INF = NaN
-   (+/-)INF / (+/-)INF = NaN
-   (+/-)INF \* 0 = NaN
-   NaN (any OP) any-value = NaN
-   The comparisons EQ, GT, GE, LT, and LE, when either or both operands is NaN returns **FALSE**.
-   Comparisons ignore the sign of 0 (so +0 equals -0).
-   The comparison NE, when either or both operands is NaN returns **TRUE**.
-   Comparisons of any non-NaN value against +/- INF return the correct result.

### Deviations or Additional Requirements from IEEE-754 Rules

-   IEEE-754 requires floating-point operations to produce a result that is the nearest representable value to an infinitely-precise result, known as round-to-nearest-even. Direct3D 10, however, defines a looser requirement: 32-bit floating-point operations produce a result that is within one unit-last-place (1 ULP) of the infinitely-precise result. This means that, for example, hardware is allowed to truncate results to 32-bit rather than perform round-to-nearest-even, as that would result in error of at most one ULP.
-   There is no support for floating-point exceptions, status bits or traps.
-   Denorms are flushed to sign-preserved zero on input and output of any floating-point mathematical operation. Exceptions are made for any I/O or data movement operation that does not manipulate the data.
-   States that contain floating-point values, such as Viewport MinDepth/MaxDepth, BorderColor values etc., may be provided as denorm values and may or may not be flushed before use by the hardware.
-   Min or max operations flush denorms for comparison, but the result may or may not be denorm flushed.
-   NaN input to an operation always produces NaN on output, however the exact bit pattern of the NaN is not required to stay the same (unless the operation is a raw move instruction - which does not alter data at all.)
-   Min or max operations for which only one operand is NaN return the other operand as the result (contrary to comparison rules above). This is a new IEEE rule (IEEE 754R), required in Direct3D 10.
-   Another new IEEE 754R rule is that min(-0,+0) == min(+0,-0) == -0, and max(-0,+0) == max(+0,-0) == +0, which honor the sign, in contrast to the comparison rules for signed zero (stated above). Direct3D 10 recommends the IEEE 754R behavior here, but it will not be enforced; it is permissible for the result of comparing zeros to be dependent on the order of parameters, using a comparison that ignores the signs.
-   x\*1.0f always results in x (except denorm flushed).
-   x/1.0f always results in x (except denorm flushed).
-   x +/- 0.0f always results in x (except denorm flushed). But -0 + 0 = +0.
-   Fused operations (such as mad, dp3) produce results that are no less accurate than the worst possible serial ordering of evaluation of the unfused expansion of the operation. Note that the definition of the worst possible ordering, for the purpose of tolerance, is not a fixed definition for a given fused operation; it depends on the particular values of the inputs. The individual steps in the unfused expansion are each allowed 1 ULP tolerance (or for any instructions Direct3D 10 calls out with a more lax tolerance than 1 ULP, the more lax tolerance is allowed).
-   Fused operations adhere to the same NaN rules as non-fused operations.
-   Multiply and divide each operate at the 32-bit floating-point precision level (accuracy to 1 ULP).

## 16-bit Floating-Point Rules

Direct3D 10 also supports 16-bit representations of floating-point numbers.

Format:

-   1 sign bit (s)in the MSB bit position
-   5 bits of biased exponent (e)
-   10 bits of fraction (f), with an additional hidden bit

A float16 value (v) follows the following rules:

-   if e == 31 and f != 0, then v is NaN regardless of s
-   if e == 31 and f == 0, then v = (-1)s\*infinity (signed infinity)
-   if e is between 0 and 31, then v = (-1)s\*2(e-15)\*(1.f)
-   if e == 0 and f != 0, then v = (-1)s\*2(e-14)\*(0.f) (denormalized numbers)
-   if e == 0 and f == 0, then v = (-1)s\*0 (signed zero)

32-bit floating-point rules also hold for 16-bit floating-point numbers, adjusted for the bit layout described above. Exceptions to this include:

-   Precision: Unfused operations on 16-bit floating-point numbers produce a result that is the nearest representable value to an infinitely-precise result (round to nearest even, per IEEE-754, applied to 16-bit values). 32-bit floating-point rules adhere to 1 ULP tolerance, 16-bit floating-point rules adhere to 0.5 ULP for unfused operations, and 0.6 ULP for fused operations.
-   16-bit floating-point numbers preserve denorms.

## 11-bit and 10-bit Floating-Point Rules

Direct3D 10 also supports 11-bit and 10-bit floating-point formats.

Format:

-   No sign bit
-   5 bits of biased exponent (e)
-   6 bits of fraction (f) for an 11-bit format, 5 bits of fraction (f) for a 10-bit format, with an additional hidden bit in either case.

A float11/float10 value (v) follows the following rules:

-   if e == 31 and f != 0, then v is NaN
-   if e == 31 and f == 0, then v = +infinity
-   if e is between 0 and 31, then v = 2(e-15)\*(1.f)
-   if e == 0 and f != 0, then v = \*2(e-14)\*(0.f) (denormalized numbers)
-   if e == 0 and f == 0, then v = 0 (zero)

32-bit floating-point rules also hold for 11-bit and 10-bit floating-point numbers, adjusted for the bit layout described above. Exceptions include:

-   Precision: 32-bit floating-point rules adhere to 0.5 ULP.
-   10/11-bit floating-point numbers preserve denorms.
-   Any operation that would result in a number less than zero, is clamped to zero.

## Related topics

<dl> <dt>

[Resources (Direct3D 10)](d3d10-graphics-programming-guide-resources.md)
</dt> </dl>

 

 



