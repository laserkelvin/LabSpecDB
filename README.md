# LabSpecDB

## A git repository for managing spectroscopic frequencies

There are two folders: `catalog` and `input`. Please put the right file in
the right place!

---

## Formatting of the files

Catalog files can have two file extensions: `.list` or `.cat`

### List files

These are either a list of frequencies, or `x,y` column format with frequency
and intensity.

### Catalog files

1. In the format of SPCAT
2. Intensities calculated at 300 K
3. If available, the `.par`, `.var`, `.lin`, and `.int` files in the folder
`input`

_Naming convention:_

1. Capital letter atoms
2. Separated by underscores
3. Vibrational states are referenced by digits, with the index corresponding
to the normal modes ordered by __frequency__:
    - For a triatomic:
        - _000_ is the ground state,
        - _010_ is $\nu_2=1$ (_NOT_ the bend!)
4. Isotopologues
    - Mass + Atom
    - e.g. _13C_

Example for $\mathrm{C_2S}$ vibrational ground state, normal species:

C2S_00000.cat

Example for $\mathrm{C_2S}$ with one $^{13}$C, $\nu_4=2$:
C2S_00020_C13.list

