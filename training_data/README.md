---
license: openrail
task_categories:
- text-generation
- question-answering
language:
- en
tags:
- medical
size_categories:
- 1K<n<10K
---

# Amod/mental_health_counseling_conversations

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)

## Dataset Description

- **Homepage:**
- **Repository:**
- **Paper:** Bertagnolli, Nicolas (2020). Counsel chat: Bootstrapping high-quality therapy data. Towards Data Science. https://towardsdatascience.com/counsel-chat
- **Leaderboard:**
- **Point of Contact:**

### Dataset Summary

This dataset is a collection of questions and answers sourced from two online counseling and therapy platforms. The questions cover a wide range of mental health topics, and the answers are provided by qualified psychologists. The dataset is intended to be used for fine-tuning language models to improve their ability to provide mental health advice.

### Supported Tasks and Leaderboards

The dataset supports the task of text generation, particularly for generating advice or suggestions in response to a mental health-related question.

### Languages

The text in the dataset is in English.

## Dataset Structure

### Data Instances

A data instance includes a 'Context' and a 'Response'. 'Context' contains the question asked by a user, and 'Response' contains the corresponding answer provided by a psychologist.

### Data Fields

- 'Context': a string containing the question asked by a user
- 'Response': a string containing the corresponding answer provided by a psychologist

### Data Splits

The dataset has no predefined splits. Users can create their own splits as needed.

## Dataset Creation

### Curation Rationale

This dataset was created to aid in the development of AI models that can provide mental health advice or guidance. The raw data was meticulously cleaned to only include the conversations.

### Source Data

The data was sourced from two online counseling and therapy platforms. The raw data can be found [here](https://github.com/nbertagnolli/counsel-chat/tree/master/data).

### Annotations

The dataset does not contain any additional annotations.

### Personal and Sensitive Information

The dataset may contain sensitive information related to mental health. All data was anonymized and no personally identifiable information is included.