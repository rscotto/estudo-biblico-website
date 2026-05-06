import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const bookSchema = z.object({
  id: z.string(),
  num: z.string(),
  title: z.string(),
  abbr: z.string(),
  author: z.string().optional(),
  chars: z.array(z.string()).optional(),
  tags: z.array(z.string()),
  body: z.string(),
  verse: z.string().optional(),
  translation: z.enum(['NAA', 'ESV']),
  order: z.number(),
  category: z.enum(['pen','his','poe','mai','men','eva','ato','pau','ger','apo']),
  cellAbbr: z.string(),
});

const books = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/books' }),
  schema: bookSchema,
});

export const collections = { books };
