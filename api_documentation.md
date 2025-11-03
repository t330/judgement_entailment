# API Documentation

Simple Django API for sentence generation and entailment checking.

## Base URL
```
http://localhost:8000
```

## Endpoints

### generate_sentences/
**GET** `/generate_sentences/`

Generates sentence pairs using AI.

**Parameters:**
- `batch=true` (optional) - Generate multiple pairs of sentences

**Response:**

#### Single pair of sentences
```json
{
  "sentences": [
    {
      "sentence1": "私は猫が大好きだ。",
      "sentence2": "猫が好きです。"
    }
  ]
}
```

#### Multiple pairs of sentences
```json
{
  "sentences": [
    {
      "sentence1": "私は猫が大好きだ。",
      "sentence2": "猫が好きです。"
    },
    {
      "sentence1": "天気が良いですね。",
      "sentence2": "あの人は美しいです。"
    },
    {
      "sentence1": "明日、会いに行くつもりです。",
      "sentence2": "明日、魚を食べるつもりです。"
    },
  ]
}
```

**Example:**

#### Generate single sentence pair
```bash
curl http://localhost:8000/generate_sentences/
```

#### Generate multiple sentence pairs (batch mode)
```bash
curl http://localhost:8000/generate_sentences/?batch=true
```

### judge/
**POST** `/judge/`

Checks if two sentences have entailment relationship.

**Headers:**
- `Content-Type: application/json`
- `X-CSRFToken: <csrf_token>` (required for CSRF protection)

**Request Body:**

#### Receive entailment judment for single sentence pair

```json
{
  "sentences": [
    {
      "sentence1": "私は猫が大好きだ。",
      "sentence2": "猫が好きです。"
    }
  ]
}
```

**Response:**
```json
{
  "label": "ENTAIL",
  "score": 0.90
}
```

#### Receive entailment judment for multiple sentence pairs

**Request Body:**
```json
{
  "sentences": [
    {
      "sentence1": "私は猫が大好きだ。",
      "sentence2": "猫が好きです。"
    },
    {
      "sentence1": "天気が良いですね。",
      "sentence2": "あの人は美しいです。"
    },
    {
      "sentence1": "明日、会いに行くつもりです。",
      "sentence2": "明日、魚を食べるつもりです。"
    },
  ]
}
```

**Response Format:**
```json
{
  "results": [
    {
      "label": "ENTAIL",
      "score": "0.90"
    },
    {
      "label": "NO_ENTAIL",
      "score": "0.30"
    },
    {
      "label": "NO_ENTAIL",
      "score": "0.40"
    }
  ]
}
```
