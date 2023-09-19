const formatterBRL = new Intl.NumberFormat('pt-BR', {
  style: 'currency',
  currency: 'BRL'
});

export function formatCurrency(value: number) {
  return formatterBRL.format(value);
}
