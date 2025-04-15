# admlist

## Gale–Shapley Algorithm for Admission List

This program implements a propose-and-reject algorithm (similar to the Gale–Shapley algorithm) for matching applicants to university majors based on their preferences and scores.

### Function Signature
```python
admission_list(applicant_list: list = [], major_dict: dict = {})
```

### Description

This function performs an applicant-major matching process based on:

- **Applicant preferences** (indicated by priority).
- **Scores** for each major.
- **Vacancies** for each major.

### Input

#### Applicants List

A list of lists, where each sublist contains the following information about an applicant:

```python
[
    [<name>, <score>, <preference_number>, <major_name>],
    ...
]
```

**Example:**
```python
[
    ['Barbie', 200, 1, 'dom_01'],
    ['Barbie', 288, 2, 'dom_03'],
    ['35397934', 234, 2, 'dom_02'],
    ['35397934', 254, 4, 'dom_01'],
    ['Boris', 277, 6, 'dom_03'],
    ['Boris', 245, 2, 'dom_02'],
    ['Boris', 277, 1, 'dom_01'],
    ['Alex', 248, 1, 'dom_02'],
    ['Alex', 285, 3, 'dom_01'],
    ['Alex', 255, 2, 'dom_03'],
    ['Ken', 248, 1, 'dom_02'],
    ['Ken', 255, 2, 'dom_03'],
    ['Ken', 276, 3, 'dom_02'],
    ['XXX', 246, 1, 'dom_01'],
    ['XXX', 246, 2, 'dom_03'],
    ['15931546', 244, 10, 'dom_02']
]
```

#### Major Dictionary

A dictionary specifying available majors and the number of available spots in each.

**Example:**
```python
{
    'dom_01': 3, 
    'dom_02': 1, 
    'dom_03': 2
}
```

### How It Works

- Applicants propose to their preferred majors.
- Majors accept the top scoring applicants up to their capacity.
- If an applicant does not get accepted into any major, they remain unmatched.
- The algorithm continues until no further changes occur.

### Default Behavior

If no arguments are passed to the function, it runs using the sample applicant list and major dictionary provided above.

### Have fun experimenting with different numbers of majors and applicants!