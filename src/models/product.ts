import type { Promotion } from './promotion';

export class Product {
  id!: number;
  name!: string;
  description!: string;
  price!: number;
  image!: string;
  promotions!: Promotion[];
  bestPromotion!: Promotion;
}
