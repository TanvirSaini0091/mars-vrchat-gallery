export interface Friend {
  id: string
  name_en: string
  name_zh?: string
}

export interface World {
  id: string
  name_en: string
  name_zh?: string
}

export interface GalleryImage {
  id: number
  filename: string
  captured: string
  world: string
  description_en?: string
  description_zh?: string
  friend: string[]
  linked?: number[]
  parent?: number
}

export interface GalleryRow {
  photo: GalleryImage
  linkedPhotos: GalleryImage[]
}
